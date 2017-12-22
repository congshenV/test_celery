"""test_celery URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from views import ansible

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^main/',ansible.main),
    url(r'^task/',ansible.task),
    url(r'^ansible_adhoc/',ansible.adhoc),
    url(r'^result/',ansible.result),
    url(r'^add/',ansible.add_view),
    url(r'^periodtask/',ansible.periodtask),
    url(r'^periodtask_add/',ansible.periodtask_add),
    url(r'^periodtask_del/',ansible.periodtask_del),
    url(r'^periodtask_delete/',ansible.periodtask_delete),
    url(r'^periodtask_list/',ansible.periodtask_list),
]
