#!/usr/bin/python3
import MySQLdb
import sys
def list_all_states(username,password,database):
        db = MySQLdb.connect(host='localhost',\
            port=3306,\
            user=username,\
            passwd=password,\
            db=database)
        cursor=db.cursor()
        cursor.execut("SELECT * FROM states ORDER BY ASC")
        rows=cursor.fechall()
        for row in rows:
            print(row)
        db.close()


if _name_=="_main_":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    list_states(username, password, database)


