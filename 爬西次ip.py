import requests
import csv
import lxml
import os
from lxml import etree
# from copyheaders import headers_raw_to_dict
import json



headers = {
"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
"Accept-Encoding":"gzip,deflate,br",
"Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8",
"Cache-Control":"max-age=0",
"Connection":"keep-alive",
"Cookie":"_free_proxy_session=BAh7B0kiD3Nlc3Npb25faWQGOgZFVEkiJWFlYmZhYzBjOWUyMzJmMjFjNGZlYjhkMmYyMzA2MTMwBjsAVEkiEF9jc3JmX3Rva2VuBjsARkkiMWk3R2FPQzQ1WVdpVkhUdG1rV1cwejdnUlkrbThiWjNxTllYeVdyakFXS1k9BjsARg%3D%3D--3ab2a9dd03c7427c31e297b23cc1cfa17ece6393; Hm_lvt_0cf76c77469e965d2957f0553e6ecf59=1544782490; Hm_lpvt_0cf76c77469e965d2957f0553e6ecf59=1545034641"
"Referer:" "https://www.xicidaili.com/api",
"Upgrade-Insecure-Requests":"1",
"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
}

class Getip(object):
    def __init__(self):
        """初始化变量"""
        self.url = 'http://www.xicidaili.com/nn/'
        self.check_url = 'https://www.ip.cn/'
        self.ip_list = []

    @staticmethod
    def get_html(url):
        """请求html页面信息"""
        headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding": "gzip,deflate,br",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
            "Cache-Control": "max-age=0",
            "Connection": "keep-alive",
            "Cookie": "_free_proxy_session=BAh7B0kiD3Nlc3Npb25faWQGOgZFVEkiJWFlYmZhYzBjOWUyMzJmMjFjNGZlYjhkMmYyMzA2MTMwBjsAVEkiEF9jc3JmX3Rva2VuBjsARkkiMWk3R2FPQzQ1WVdpVkhUdG1rV1cwejdnUlkrbThiWjNxTllYeVdyakFXS1k9BjsARg%3D%3D--3ab2a9dd03c7427c31e297b23cc1cfa17ece6393; Hm_lvt_0cf76c77469e965d2957f0553e6ecf59=1544782490; Hm_lpvt_0cf76c77469e965d2957f0553e6ecf59=1545034641"
                      "Referer:" "https://www.xicidaili.com/api",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
        }
        try:
            respones = requests.get('https://www.xicidaili.com/nn/', headers=headers).content.decode()
            selector = etree.HTML(respones)
            html = selector.xpath('//tr[@class="odd"]')[2:]
            return html
        except Exception as e:
            return ''

    def get_avai_ip(self,ip_address,ip_port):
        headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding": "gzip,deflate,br",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
            "Cache-Control": "max-age=0",
            "Connection": "keep-alive",
            "Cookie": "_free_proxy_session=BAh7B0kiD3Nlc3Npb25faWQGOgZFVEkiJWFlYmZhYzBjOWUyMzJmMjFjNGZlYjhkMmYyMzA2MTMwBjsAVEkiEF9jc3JmX3Rva2VuBjsARkkiMWk3R2FPQzQ1WVdpVkhUdG1rV1cwejdnUlkrbThiWjNxTllYeVdyakFXS1k9BjsARg%3D%3D--3ab2a9dd03c7427c31e297b23cc1cfa17ece6393; Hm_lvt_0cf76c77469e965d2957f0553e6ecf59=1544782490; Hm_lpvt_0cf76c77469e965d2957f0553e6ecf59=1545034641"
                      "Referer:" "https://www.xicidaili.com/api",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
        }

        ip_url_next = '://' + ip_address + ':' + ip_port
        proxies = {'http': 'http' + ip_url_next, 'https': 'https' + ip_url_next}

        try:
            r = requests.get(self.check_url, headers=headers, proxies=proxies, timeout=3)
            html = r.text
        except:
            print('fail-%s' % ip_address)
        else:
            print('success-%s' %ip_address)
            ip_info = {'address': ip_address, 'port': ip_port}
            self.ip_list.append(ip_info)


    def main(self):
        """主方法"""
        respones = requests.get(url=self.url, headers=headers).content.decode()
        selector = etree.HTML(respones)
        #     html = selector.xpath('//tr[@class="odd"]')[2:]
        html = selector.xpath('//tr[@class="odd"]')[2:]
        for xici in html:
                ip_address = xici.xpath('./td[2]/text()')[0]
                ip_port = xici.xpath('./td[3]/text()')[0]
                # add = xici.xpath('./td[4]/a/text()')[0]
                # anonymous = xici.xpath('./td[@class="country"][2]/text()')[0]
                # type = xici.xpath('./td[6]/text()')[0]
                # s_time = xici.xpath('./td[9]/text()')[0]
                # t_time = xici.xpath('./td[10]/text()')[0]

                self.get_avai_ip(ip_address,ip_port)

        with open("ip.txt", mode="w", encoding="utf-8") as d:
            json.dump(self.ip_list, d)
        print(self.ip_list)

        #
        # # 写入有效文件
        # with open('ip.txt', 'w') as file:
        #     json.dump(self.ip_list, file)
        # print(self.ip_list)

# 主程序入住
if __name__ == '__main__':
    get_ip = Getip()
    get_ip.main()




#####################函数编程
# def star_request():
#     respones = requests.get('https://www.xicidaili.com/nn/', headers=headers).content.decode()
#     selector = etree.HTML(respones)
#     html = selector.xpath('//tr[@class="odd"]')[2:]
#
#     item_list = []
#     for xici in html:
#             ip = xici.xpath('./td[2]/text()')[0]
#             port = xici.xpath('./td[3]/text()')[0]
#             add = xici.xpath('./td[4]/a/text()')[0]
#             anonymous = xici.xpath('./td[@class="country"][2]/text()')[0]
#             type = xici.xpath('./td[6]/text()')[0]
#             s_time = xici.xpath('./td[9]/text()')[0]
#             t_time = xici.xpath('./td[10]/text()')[0]
#
#
#
#             proxies = {'http://': ip,
#                       'https://': ip,
#                       }
#             try:
#                 respones1 = requests.get('http://www.baidu.com',headers=headers, proxies=proxies,timeout=3)
#                 if respones1.status_code == 200:
#                     print(ip +":"+ port)
#                     with open("ip.txt", mode="a+", encoding="utf-8") as d:
#                         d.write(ip + "\n")
#             except Exception:
#                 print("不可用", ip , Exception)
#
#             iteam = {'ip':ip,
#                     'port': port,
#                     'add' : add,
#                     'anonymous': anonymous,
#                     'type': type,
#                     's_time': s_time,
#                     't_time': t_time
#                      }
#
#             item_list.append(iteam)
#             # print(item_list)
#
#     with open('ip.csv','w',encoding='utf-8') as f:
#         write = csv.DictWriter(f, fieldnames=['ip','port','add','anonymous','type','s_time','t_time'])
#         write.writeheader()
#         write.writerows(item_list)
#
# star_request()


