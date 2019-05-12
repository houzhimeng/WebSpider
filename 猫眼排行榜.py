import requests
import re

def get_one_page(url):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        return None

def parse_one_page(html):
    pattern = re.compile('<dd>.*?board-index.*?>(.*?)</i>.*?=“(.*?)”name.*?a.*?</a>', re.S)
    items = re.findall(pattern, html)
    print(items)

def main():
    url = 'https://maoyan.com/board/4'
    html = get_one_page(url)
    print(html)

if __name__ == '__main__':
    main()

