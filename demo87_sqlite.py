import sqlite3

connection1 = sqlite3.connect('db\\sqlite3_lab1.sqlite')
print "open db success"
drop_sql = 'DROP TABLE IF EXISTS EMPLOYEE;'
create_sql = '''
CREATE TABLE EMPLOYEE
(ID INTEGER PRIMARY KEY,
 NAME TEXT NOT NULL,
 AGE INT NOTE NULL,
 DEPT INT,
 ADDRESS CHAR(50)
 );
'''
print "clean up db"
connection1.execute(drop_sql)
print "create db"
connection1.execute(create_sql)
connection1.close()