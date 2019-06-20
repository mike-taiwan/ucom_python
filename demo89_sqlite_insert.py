import sqlite3

connection1 = sqlite3.connect('db\\sqlite3_lab1.sqlite')

employees = [{'NAME': 'Mark', "AGE": 38, 'DEPT': 1, 'ADDR': 'Taipei'},
             {'NAME': 'John', "AGE": 43, 'DEPT': 2, 'ADDR': 'Hsinchu'},
             {'NAME': 'James', "AGE": 47, 'DEPT': 1, 'ADDR': 'Taipei'}]

INSERT_DML = "INSERT INTO EMPLOYEE(NAME, AGE, DEPT, ADDRESS) VALUES(?,?,?,?)"

for e in employees:
    connection1.execute(INSERT_DML, (e['NAME'],e['AGE'],e['DEPT'],e['ADDR']));
    print ".",

print

connection1.commit()
connection1.close()