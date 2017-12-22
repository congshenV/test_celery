#!/bin/bash
process=`ps -ef |grep worker_|awk '{print $2}'`
for i in $process;
do
    if [ $i -eq 1 ];then
        echo "do nothing"
    else
        kill -9 $i
    fi
done
