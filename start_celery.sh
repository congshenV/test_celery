#!/bin/bash
process=`ps -ef |grep -E "./manage.py celery worker -c 10 --autoreload" |awk '{print $2}'`
redis-cli config set stop-writes-on-bgsave-error no
for i in $process;
do
    if [ $i -eq 1 ];then
        echo "do nothing"
    else
        kill -9 $i
    fi
done
./manage.py celery purge -f;./manage.py celery worker -c 10 --autoreload

export C_FORCE_ROOT=True
./manage.py celery worker -A test_celery -l info -n worker_low1 -Q low_queue
./manage.py celery worker -A test_celery -l info -n worker_low2 -Q low_queue
./manage.py celery worker -A test_celery -l info -n worker_low3 -Q low_queue

./manage.py celery worker -A test_celery -l info -n worker_high1 -Q high_queue -c 1

