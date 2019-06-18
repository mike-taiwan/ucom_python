# encoding=UTF-8
import json

l1 = ['.NET', 'Oracle', 'Cloudera', '資安']
print type(l1)
ret1 = json.dumps(l1)
print type(ret1), ret1

d1 = {'course': 'bdpy', 'location': 'TPE', 'duration': 35, 'instructor': 'Mark HO'}
print type(d1)
ret2 = json.dumps(d1)
print type(ret2), ret2

ret3 = json.loads(ret1)
print type(ret3)
for x in ret3:
    print x,
print
ret4 = json.loads(ret2)
print type(ret4)
for y in ret4:
    print y,ret4[y]
print