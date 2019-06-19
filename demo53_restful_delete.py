# encoding=UTF-8
import requests

base_url = 'https://ucom-4fdd3.firebaseio.com/%s.json'
url1 = base_url % 'demo1'
url2 = base_url % 'demo2'
url3 = base_url % 'demo3'
url4 = base_url % 'demo4'
url5 = base_url % 'demo5'
url6 = base_url % 'demo6'

# r1 = requests.delete(url1)
# print r1.status_code
# r2 = requests.delete(url2)
# print r2.status_code
# r3 = requests.delete(url3)
# print r3.status_code
# r4 = requests.delete(url4)
# print r4.status_code
# r5 = requests.delete(url5)
# print r5.status_code
# r6 = requests.delete(url6)
# print r6.status_code
all_url = base_url%""
rall = requests.delete(all_url)
print rall.status_code