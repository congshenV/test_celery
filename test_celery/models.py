from django.db import models

class Adhoc(models.Model):
    task_id = models.CharField(max_length=128)
    first = models.CharField(max_length=128)
    second = models.CharField(max_length=128)
    log_date = models.DateTimeField()

class Ansible(models.Model):
    task_id = models.CharField(max_length=128)
    hosts = models.CharField(max_length=128)
    command = models.CharField(max_length=128)
    log_date = models.DateTimeField()

