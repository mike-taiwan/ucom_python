import requests
from bs4 import BeautifulSoup

url1 = 'https://www.mobile01.com/'
headers = {'User-Agent': 'my super browser', 'from': 'xyz@uuu.com'}
r1 = requests.get(url1, headers=headers)
soup = BeautifulSoup(r1.content, "html.parser")
hot = soup.find('div', {'id': 'hot-posts'})
hot_links = hot.find_all('a')
for link in hot_links:
    print link
# 'https://www.mobile01.com/category.php?id=4'
# https://www.mobile01.com/category.php?id=2
# https://www.mobile01.com/category.php?id=6
base_url = 'https://www.mobile01.com/category.php?id=%d'
board_ids = [2, 4, 6]
for id in board_ids:
    url = base_url % id
    headers = {'User-Agent': 'my super browser', 'from': 'xyz@uuu.com'}
    r1 = requests.get(url, headers=headers)
    soup = BeautifulSoup(r1.content, "html.parser")
    print "####",soup.title,'####'
    hot = soup.find('div', {'id': 'hot-posts'})
    hot_links = hot.find_all('a')
    for link in hot_links:
        print link