# encoding=UTF-8

import requests

base_url = 'https://ucom-4fdd3.firebaseio.com/%s.json'
url1 = base_url % 'demo1'
url2 = base_url % 'demo2'
url3 = base_url % 'demo3'
url4 = base_url % 'demo4'
url5 = base_url % 'demo5'
url6 = base_url % 'demo6'

r1 = requests.get(url1)
print r1.status_code, r1.content
r2 = requests.get(url2)
print r2.status_code, r2.content
r3 = requests.get(url3)
print r3.status_code, r3.content

r4 = requests.get(url4)
print r4.status_code, type(r4.content), len(r4.content), r4.content[:10]
print type(r4.json()), r4.json()
for item in r4.json():
    print item,
print

r5 = requests.get(url5)
print type(r5.content), type(r5.json())
for k, v in r5.json().items():
    print 'k=%s,v=%s' % (str(k), str(v))

r6 = requests.get(url6)
print type(r6.json())
for record in r6.json().values():
    print type(record)
    for k,v in record.items():
        print 'item key=%s, value=%s'%(str(k), str(v))