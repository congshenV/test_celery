from __future__ import absolute_import
from celery import shared_task
import time
import commands
from celery.result import AsyncResult
from celery.task.control import revoke

@shared_task(track_started=True)
def add(x, y):
    time.sleep(15)
    return x + y

@shared_task
def ansible_adhoc( hosts , module='-m command', command=''):
    #time.sleep(20)
    cmd = 'ansible ' + hosts + ' ' + module+' -a "' +  command + '"'
    (stat, result) = commands.getstatusoutput(cmd)
    if stat == 0 :
        return result
    else :
        raise Exception(result)

@shared_task(track_started=True)
def backup(instance):
    print "start backup ..."
    time.sleep(instance)
    print "finished backup!"
    if instance > 30 :
        recover.delay(instance)
        return "OK"
    return "unOK"

@shared_task(track_started=True)
def recover(instance):
    print "start recover..."
    time.sleep(instance)
    print "finished recover!"
    if instance > 60 :
        return "OK"
    backup.delay(instance)
    return "unOK"

@shared_task(track_started=True)
def redis_install(hosts, type, port, size, use, pw_rule, role, autorw):
    #time.sleep(20)
    module = '-m command'
    cmd1 = 'wget http://***/redis_env_init.sh -O /root/scripts/redis_env_init.sh'
    cmd2 = 'wget http://***/redis_install.sh -O /root/scripts/redis_install.sh'
    cmd3 = "/root/scripts/redis_install.sh -i %s -p %s -m %s -t %s -a %s -r %s -w %s" % (type, str(port), str(size), use, pw_rule, role, autorw)
    ansible_cmd = 'ansible ' + hosts + ' ' + module+' -a "' +  cmd3 + '"'
    (stat, result) = commands.getstatusoutput(ansible_cmd)
    if stat == 0 :
        return result
    else :
        raise Exception(result)

@shared_task(track_started=True)
def tcollector_update(hosts, src_file):
    #time.sleep(20)
    module = '-m copy'

    cmd = "src='/home/dba_redis/%s' dest='/usr/local/tcollector/collectors/0/%s' mode=\"u+x,g+x,o+x\"" % (src_file, src_file)

    ansible_cmd = 'ansible ' + hosts + ' ' + module+' -a "' +  cmd + '"' + " -s"

    module = '-m shell'
    cmd2 = "cd /usr/local/tcollector/&&nohup /usr/local/tcollector/tcollector restart &"
    ansible_cmd2 = 'ansible ' + hosts + ' ' + module+' -a "' +  cmd2 + '"' + " -s"

    (stat, result) = commands.getstatusoutput(ansible_cmd)
    (stat2, result2) = commands.getstatusoutput(ansible_cmd2)
    if stat == 0 and stat2 == 0:
        return result,result2
    else :
        raise Exception(result)
