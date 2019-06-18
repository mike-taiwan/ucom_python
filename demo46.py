import requests
import bs4

url1 = 'https://www.uuu.com.tw/'
result1 = requests.get(url1)
soup1 = bs4.BeautifulSoup(result1.content, 'html.parser')
print soup1.title
courses = soup1.find('div', {'id': 'course_list'})
course_titles = courses.find_all('h3')
for t in course_titles:
    print t