#__*__coding:utf-8__*__

from celery.result import AsyncResult
from django.shortcuts import render_to_response
from djcelery.models import PeriodicTask
import json
from djcelery import models as celery_models
from tools.tasks import add,ansible_adhoc
from test_celery.models import Adhoc,Ansible
from tools.db import Db
import datetime


def main(request):
    return  render_to_response('main.html')

def task(request):
    return  render_to_response('task.html')

def periodtask(request):
    return  render_to_response('periodtask.html')

def periodtask_delete(request):
    return  render_to_response('periodtask_del.html')

def adhoc(request):
    hosts = request.GET.get('hosts')
    module = request.GET.get('module')
    command = request.GET.get('command')
    result = ansible_adhoc.delay(hosts, module, command)
    db_con = Ansible(task_id=result.id,hosts=hosts,command=command,log_date=datetime.datetime.now())
    db_con.save()
    return render_to_response('task.html')

def add_view(request):
    hosts = request.GET.get('hosts')
    command = request.GET.get('command')
    result = add.delay(int(hosts),int(command))
    db_con = Ansible(task_id=result.id,hosts=hosts,command=command,log_date=datetime.datetime.now())
    db_con.save()
    return render_to_response('task.html')

def periodtask_add(request):
    name = request.GET.get('name')
    task = request.GET.get('task')
    task, created = celery_models.PeriodicTask.objects.get_or_create(name=name, task=task)
    task_args = {"hosts": request.GET.get('hosts'), "module":request.GET.get('module'), "command": request.GET.get('command')}
    task.kwargs = json.dumps(task_args)
    #crontab_time={"month_of_year":'*',"day_of_month":"*","hour":"*","minute":59}
    crontab_str = request.GET.get('crontab')
    crontab_str = crontab_str.split()
    #crontab = celery_models.CrontabSchedule()
    crontab_map={"minute":crontab_str[0],"hour":crontab_str[1],"day_of_week":crontab_str[2],"day_of_month":crontab_str[3],"month_of_year":crontab_str[4]}
    #crontab.minute = crontab_str[0]
    #crontab.hour = crontab_str[1]
    #crontab.day_of_week = crontab_str[2]
    #crontab.day_of_month = crontab_str[3]
    #crontab.month_of_year = crontab_str[4]
    #interval = eval(request.GET.get('interval'))
    #interval = celery_models.IntervalSchedule.objects.create(**interval)
    #task.interval = interval
    crontab,created = celery_models.CrontabSchedule.objects.get_or_create(**crontab_map)
    task.crontab = crontab
    task.enabled = True
    task.save()
    return render_to_response('periodtask.html')

def periodtask_del(request):
    name = request.GET.get('name')
    task = request.GET.get('task')
    task, created = celery_models.PeriodicTask.objects.get_or_create(name=name, task=task)
    task.delete()
    return render_to_response('periodtask_del.html')

# 任务结果
def result(request):
    #查询所有的任务信息
    db = Db()
    rows = db.get_tasksinfo("ansible")
    return render_to_response('result.html',{'rows':rows})

def periodtask_list(request):
    #list = celery_models.PeriodicTask.objects.all()
    db = Db()
    rows = db.get_periodtask_list()
    return render_to_response('periodtask_list.html',{'rows':rows})

