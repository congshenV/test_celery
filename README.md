# celery test


# celery API

For more info, see the [celery API Documentation](http://docs.celeryproject.org/en/master/reference/celery.html)


# 环境

- python = 2.7.12
- ansible (2.3.1.0)
- django-celery (3.2.1)                pip install django-celery
- celery (3.1.25)
- Django (1.11.3)
- flower (0.9.2)
- MySQL-python (1.2.3rc1)
- redis (2.10.5)
# 部署启动

**将此项目同步到相应的机器上：**

```
然后是创建数据表并创建超级用户
在mysql中创建数据库
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
具体操作参见  celery大全.html、celery操作记录.html

```

*NOTE: 具体的参数在./test_celery/setting.py里，主要查看有些数据需要根据机器来修改*

# 文件结构说明，只列重要的
```
.
├── kill_worker.sh   快速杀死worker的脚本
├── manage.py        管理脚本，不需要修改
├── start            启动指令放在这里
├── start_celery.sh  启动worker的指令
├── test_celery      celery项目的主要内容
│   ├── celery.py    celery实例
│   ├── models.py    数据库模型
│   ├── settings.py  配置
│   ├── templates    html文件
│   │   ├── main.html
│   │   ├── periodtask_del.html
│   │   ├── periodtask.html
│   │   ├── periodtask_list.html
│   │   ├── result.html
│   │   └── task.html
│   ├── urls.py      url注册
│   ├── views        url对应的函数接口
│   │   ├── ansible.py
│   ├── wsgi.py
└── tools
    ├── db.py        自己封装的数据库操作api
    ├── tasks.py     celery任务实现
```

需要配置的内容：
1、setting   broker地址、database地址
2、改一下templates里面的html，现在用的都是静态链接，地址都是写死的····所以大家在网页链接跳转出现问题就需要改下里面的跳转链接



访问接口：
ip:port/main
django-admin:  ip:port/admin

# author

yycmessi@163.com
