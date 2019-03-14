import requests
import lxml.html
import csv
from lxml import etree

# headers = {
#     'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
#     'accept-encoding': 'gzip, deflate, br',
#     'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
#     'cache-control': 'max-age=0',
#     'cookie': '_uab_collina=154487149236313236065558; cna=rZKFFIggLH8CAT0wP0n4ULvz; x_hm_tuid=Fe22ONZisgzKxihUbM5nIjP0WImDDjHpwsZBfSSXciwiGlVl3sZ4uDLtOaGmqnKg; UM_distinctid=167b19c699b248-0c86bba9f191ed-10336653-1aeaa0-167b19c699cc49; cn_7415364c9dab5n09ff68_dplus=%7B%22distinct_id%22%3A%20%22167b19c699b248-0c86bba9f191ed-10336653-1aeaa0-167b19c699cc49%22%2C%22sp%22%3A%20%7B%22%24_sessionid%22%3A%200%2C%22%24_sessionTime%22%3A%201544873084%2C%22%24dp%22%3A%200%2C%22%24_sessionPVTime%22%3A%201544873084%7D%2C%22initial_view_time%22%3A%20%221544870796%22%2C%22initial_referrer%22%3A%20%22https%3A%2F%2Fwww.damai.cn%2F%3Fspm%3Da2oeg.project.top.dhome.6b654e6ewU4NBz%22%2C%22initial_referrer_domain%22%3A%20%22www.damai.cn%22%7D; x5sec=7b226d65632d67756964652d7765623b32223a2261376661336130643331396539663434653131363733313865326135303462364349334f302b4146454a717168626e7a6f49364a45773d3d227d; isg=BHt7DS2Bo5aeBp8igyykyLRpClkleL0jqi3gFG04V3qRzJuu9aAfIpkO4iwnbOfK',
#     'referer': 'https://search.damai.cn/',
#     'upgrade-insecure-requests': '1',
#     'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
# }


contents = requests.get('http://www.ttplus.cn').content
html = lxml.html.fromstring(contents)

htmls = html.xpath('//div[@id="m-news-list"]/a[@class="m-news-list-item m-news-box clearfix"]/div[@class="m-news-box-bd"]')

item_list = []
iteam = {}
title = html.xpath('//div[@class="m-news-box-bd"]/h3/text()')
titles = {'title': title}
print(titles)
name = html.xpath('//div[@class="m-news-box-bd"]/p[@class="m-news-box-ifo clearfix"]/span[@class="m-news-author"]/text()')
time = html.xpath('//div[@class="m-news-box-bd"]/p[@class="m-news-box-ifo clearfix"]/span[@class="m-news-time"]/text()')

for i in range(len(title)):
    result = {'title': title[i],
              'name': name[i],
              'time': time[i]
    }
    print(result)
    item_list.append(result)


#2
# print(htmls)
# for ttplus in htmls:
#     hzm = {}
#     hzm['title'] = ttplus[0].xpath('///h3/text()')[0]
#     # title = titan.xpath('//div[@class="m-news-box-bd"]/h3/text()')
#     hzm['name'] = ttplus.xpath('//div[@class="m-news-box-bd"]/p[@class="m-news-box-ifo clearfix"]/span[@class="m-news-author"]/text()')[0]
#     hzm['time'] = ttplus.xpath('//div[@class="m-news-box-bd"]/p[@class="m-news-box-ifo clearfix"]/span[@class="m-news-time"]/text()')[0]
#     print(hzm)


    # titles = [ title(x) for x in len(title)]

    # iteam = {
    #     'title': title[i] [for i in range(0, len(title)) title = (title[i])}
    # print(iteam)


with open('titan.csv','w',encoding='utf-8') as f:
    write = csv.DictWriter(f, fieldnames=['title','name','time'])
    write.writeheader()
    write.writerows(item_list)