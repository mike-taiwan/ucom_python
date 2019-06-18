import requests


url1 = 'https://bugzilla.mozilla.org/rest/bug/35'
result = requests.get(url1)
print result.status_code
print (result.json())
firstBug = result.json()["bugs"][0]
print type(firstBug)
print firstBug['summary']
details = firstBug['cc_detail']
for i in details:
    print i['email']
