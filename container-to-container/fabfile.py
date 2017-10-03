from exceptions import Exception
from fabric.api import hide
from fabric.colors import green
from fabric.colors import red
from fabric.colors import yellow
from fabric.decorators import task
from fabric.operations import local
from contextlib import closing
import pymysql.cursors
import os

dbhost = os.environ.get('DB')

@task
def query_mysql():
    with closing(pymysql.connect(host=dbhost, port=3306, user="root", passwd="my-secret-pw", db='demo')) as connection:
        with connection.cursor() as cursor:
            cursor.execute("""show databases;""")
            results = cursor.fetchall()
            print green('-'*80)
            print green('databases found:')
            for db in results:
                print green(str(db[0]))
            print green('-'*80)
