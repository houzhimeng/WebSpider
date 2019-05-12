import requests
import time
import re
from lxml import html

headers = {
'Referer': 'https://www.xicidaili.com/nn/1',
'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
}
respones = requests.get("https://www.xicidaili.com/nn/1", headers=headers)


class spider(self):
    headers = {
        'Referer': 'https://www.xicidaili.com/nn/1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    }



