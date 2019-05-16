#coding:utf-8
"""
Created on 2019-05-08
@title: ''
@author: 南山南
公众号：pythonislover
"""

from bs4 import BeautifulSoup
import requests
import re
import pandas
import time

headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36',
'Cookie': 'bid=_DtbPD3fa4s; gr_user_id=06703540-fc29-4585-b68d-accc287da9ca; _vwo_uuid_v2=DB4F4F2E1E929828C395880DD37DCF949|e380830891a035234cedd541bd3a857b; __yadk_uid=XYTogG4l7Mn6tbPCGNSdUJd7S7qXY9VC; douban-fav-remind=1; viewed="30214851_4212921_3117898_30234022"; __utmz=30149280.1553823999.5.5.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmz=81379588.1553823999.4.4.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmc=30149280; __utmc=81379588; _pk_ref.100001.3ac3=%5B%22%22%2C%22%22%2C1557210749%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DBScn2OJdr9GYZ6C8S8vEzF1VIWfWEsQAAQX1HDdqIj7ulUcE71u0Ef0yZcwhDA6Yy_WeoiIes862ez9MXyk_HK%26wd%3D%26eqid%3D8fdde6090007c03d000000045c9d78e4%22%5D; _pk_id.100001.3ac3=4348bfe6c5807777.1547172790.6.1557210749.1557208133.; __utma=81379588.2103045713.1547172790.1557208133.1557210749.6; ll="118159"; __utma=30149280.1567660649.1547172790.1557210749.1557217345.8'
}

data_list=[]

def get_book_info(url):

    res = requests.get(url,headers=headers,timeout =20)
    # print(res.status_code,res.apparent_encoding,res.content,res.encoding)
    res.encoding = res.apparent_encoding
    response = res.text

    soup = BeautifulSoup(response,'lxml')

    artiche = soup.find_all('li','subject-item')

    print(artiche)

    for item in artiche:
        for i in item.find_all('div','info'):
            try:
                if i.find('a').string:     #获取书名
                    book_name = i.find('a').string.strip()
                else:
                    book_name='NULL'       #书名为空
                if  i.find('a').attrs:     #获取a标签属性
                    book_url = i.find('a').attrs.get('href').strip()   #书籍路径
                else:
                    book_url = url

                pub_info = i.find('div','pub').string.strip()   #出版信息
                book_info_list = pub_info.split('/')            #
                if len(book_info_list)==5:
                    book_auth = book_info_list[0]+','+book_info_list[1]
                    book_publish = book_info_list[2]
                    book_pub_date = book_info_list[3]
                    book_price = re.findall('\d+',book_info_list[4])[0]
                elif len(book_info_list)==4:
                    book_auth = book_info_list[0]
                    book_publish = book_info_list[1]
                    book_pub_date = book_info_list[2]
                    book_price = re.findall('\d+',book_info_list[3])[0]
                else:
                    book_auth = 'NULL'
                    book_publish = book_info_list[0]
                    book_pub_date = book_info_list[1]
                    book_price = re.findall('\d+', book_info_list[2])[0]
                        #评分
                rating_nums = i.find('span','rating_nums').string
                        #评论数信息
                comment_nums = i.find('span','pl').string.strip()
                comment_nums = re.findall('\d+',comment_nums)
                comment_nums = comment_nums[0]  #评论内容
                        #评论内容
                if i.find('p'):
                    comment_content = i.find('p').string.strip().replace('\n','')
                else:
                    comment_content= 'NULL'

                print(book_name,
                      book_url,book_auth,book_publish,
                      book_pub_date,book_price,rating_nums,
                      comment_nums,comment_content)

                data_dict = {}
                data_dict['书名'] = book_name
                data_dict['链接'] = book_url
                data_dict['作者'] = book_auth
                data_dict['出版社'] = book_publish
                data_dict['出版日期'] = book_pub_date
                data_dict['价格'] = book_price
                data_dict['评分'] = rating_nums
                data_dict['评论数'] = comment_nums
                data_dict['评论内容'] = comment_content


                data_list.append(data_dict)
            except Exception as e:
                print('程序出错了',e)

            continue

    return data_list






if __name__ == '__main__':
    time.sleep(3)
    # info = []
    for i in range(0,980,20):
    # for i in range(0,60,20):
        base_url = 'https://book.douban.com/tag/文学?start=%s&type=T'%i
        data_list_all = get_book_info(base_url)
        # info.extend(data_list_all)
    # print(data_list_all)

    # print(info)
    df = pandas.DataFrame(data_list_all)
    df.to_csv('book.csv', encoding='utf_8_sig')  # encoding解决乱码问题