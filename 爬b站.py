'''

    实时抓取哔哩哔哩网站主播直播弹幕2017-10-29

'''

import requests, time

url='https://api.live.bilibili.com/ajax/msg'  # POST请求，向这个网址提交数据

form={'csrf_token':'8a01d2d8763108707624001c595034c5',
'roomid':'5193',
'token':''
}

while True:  # text,text2主要是防止重复的弹幕
    html = requests.post(url,data=form)
    text = list(map(lambda ii:html.json()['data']['room'][ii]['text'],range(10)))
    time.sleep(5)
    html2 = requests.post(url,data=form)
    text2 = list(map(lambda ii:html2.json()['data']['room'][ii]['text'],range(10)))
    ret_list = [print(item) for item in text2 if item not in text] 
    
