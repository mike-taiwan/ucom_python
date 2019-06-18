# encoding=UTF-8
import requests

base_url = 'https://ucom-4fdd3.firebaseio.com/%s.json'
url4 = base_url % 'demo4'
url5 = base_url % 'demo5'

json4 = {'3': 'Newly added', '1': 1.23, '6': u'獅子'}
result4 = requests.patch(url4, json=json4)
print result4.status_code, result4.content

json5 = {'instructor':'Mark','duration':36}
result5 = requests.patch(url5, json=json5)
print result5.status_code, result5.content