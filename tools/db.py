import datetime
import MySQLdb
from MySQLdb.cursors import DictCursor

from test_celery.settings import DATABASES


class Db:

    def __init__(self):
        self.database = DATABASES['default']
        self.database_name = self.database['NAME']
        self.user = self.database['USER']
        self.password = self.database['PASSWORD']
        self.host = self.database['HOST']
        self.port = self.database['PORT']
        self.con = MySQLdb.connect(self.host, self.user, self.password, self.database_name, int(self.port), charset='utf8')
        self.con.autocommit(True)

    def close_connect(self):
        self.con.close()

    def get_tasksinfo(self, table):
        cur = self.con.cursor(DictCursor)
        query_str = "select b.id as id,b.task_id as task_id,b.hosts as hosts,b.command as command,b.log_date as logdate,a.status as status,a.result as result,a.traceback as traceback " \
                    "from celery_taskmeta a inner join test_celery_" + table +" b on a.task_id=b.task_id;"
        cur.execute(query_str)
        rows  = cur.fetchall()
        cur.close()
        return rows

    def get_periodtask_list(self):
        cur = self.con.cursor(DictCursor)
        query_str = "select b.id as id,b.name as name,b.task as task,b.args as args,b.kwargs as kwargs,b.queue as queue,b.exchange as exchange,b.routing_key as routing_key,b.expires as expires,b.enabled as enabled,b.last_run_at as last_run_at,b.total_run_count as total_run_count,b.date_changed as date_changed,b.crontab_id as crontab_id,b.interval_id as interval_id,concat(a.minute,a.hour,a.day_of_week,a.day_of_month,a.month_of_year) as crontab " \
                    "from djcelery_crontabschedule a inner join djcelery_periodictask b on a.id=b.crontab_id;"
        cur.execute(query_str)
        rows  = cur.fetchall()
        cur.close()
        return rows

