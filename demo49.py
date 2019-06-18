# encoding=UTF-8
import requests

base_url = 'https://ucom-4fdd3.firebaseio.com/%s.json'

url1 = base_url % 'demo1'
url2 = base_url % 'demo2'
url3 = base_url % 'demo3'
url4 = base_url % 'demo4'
url5 = base_url % 'demo5'
result1 = requests.put(url1, json='hello_world')
print result1.content, result1.status_code
result2 = requests.put(url2, json='中文的內容')
print result2.content, result2.status_code
result3 = requests.put(url3, json=u'中文的內容')
print result3.content, result3.status_code
json4 = ['hello', 123, 4.567, None, 'tiger', u'老虎']
result4 = requests.put(url4, json=json4)
print result4.content, result4.status_code
json5 = {'course': 'bdpy', 'duration': 35}
result5 = requests.put(url5, json=json5)
print result5.content, result5.status_code
