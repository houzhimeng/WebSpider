import requests
import re

# data = {'name': 'hou', 'password': '15'}
# Url= requests.post('http://exercise.kingname.info/exercise_requests_post', data=data)
# print(Url.content.decode())


get_url = requests.get('http://exercise.kingname.info/exercise_requests_get.html').content.decode()
# print(get_url)
# title = re.search('title>(.*?)<', get_url, re.S).group(1)
# print(title)
C_list = re.findall('p>(.*?)<', get_url, re.S)
# print(C_list)
C_str= '\n'.join(C_list)
print(C_str)
