#!/usr/bin/python3
import MySQLdb
import sys
def list_N(mysql username, mysql password ,database name):
    db=MySQLdb.connect(host='localhost',\
                       port=3306,\
                       user=mysql username,\
                       passwd=mysql password,\
                       db=database name)
    cursor=db.cursor()
    cursor.execute("SELECT * FROM states WHERE mysql username LIKE "N%" mysql username=""" ORDER BY id ASC")
    rows=cursor.fetchall()
    for row in rows:
        print (row)

if_name_=="_main_":
    mysql username=sys.arg[1]
    mysql password=sys.arg[2]
    database name=sys.arg[3]
    list_N(mysql username, mysql password ,database name)
