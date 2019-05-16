import requests
import socks5

proxy = '127.0.0.1:1086'
proxies = {
    'http': 'socks5://' + proxy,
    'https': 'socks5://' + proxy,
}
try:
    respones = requests.get('https://www.google.com', proxies=proxies)
    print(respones.text)
except requests.exceptions.ConnectionError as e:
    print('Error', e.args)
