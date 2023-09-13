#!/usr/bin/python3
import MySQLdb
import sys
def list_N(username, password ,database):
    db=MySQLdb.connect(host='localhost',\
                       port=3306,\
                       user= username,\
                       passwd=password,\
                       db=database)
    cursor=db.cursor()
    cursor.execute("SELECT * FROM states WHERE username LIKE 'N%' ORDER BY id ASC")
    rows=cursor.fetchall()
    for row in rows:
        print (row)

if_name_=="_main_":
    username=sys.arg[1]
    password=sys.arg[2]
    database=sys.arg[3]
    list_N(username,password ,database)
