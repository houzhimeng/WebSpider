import requests
from lxml import etree



header = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'cache-control': 'max-age=0',
    'cookie': '_zap=48356585-ec48-411b-9a66-d487b7ae607b; d_c0="ANDiMph6lw6PTvEQHMMifR0QmejqXGqazZ8=|1543463744"; l_cap_id="MjRjNWNkZDA1YWQ4NDY4MjkxMGRhYzc2OTkyNWZiNDI=|1544601803|6786e6673fe0f040c6a9223f5f4baed9721dc814"; r_cap_id="YmE5MzhmZTIyZTEzNDRmZmE2OTQwZWZjNDRjODNlNDE=|1544601803|815c2e4c7621df052c4f61ed8bfc68b51b758acd"; cap_id="MzM5MzBhMzA5ZGQ0NDkwNTg5MjFjNjkwNDgxZjM0MzA=|1544601803|6cfb19bf6f9133eff82dea3b17141cc2276e9a73"; _xsrf=h29qRM08rAMJXER3FsTSUGeR67a9bAAd; tst=r; tgw_l7_route=931b604f0432b1e60014973b6cd4c7bc; capsion_ticket="2|1:0|10:1544685115|14:capsion_ticket|44:MWNiNmVhNzc4NzUzNDJhNDhlZjgyNzk0NjRjMTk1YWM=|727a2ae3d07f83ff43bdceeeef8990f2dc9d0442e52ae6a04b8702f38c716be5"; z_c0="2|1:0|10:1544685155|4:z_c0|92:Mi4xSkxzaEFnQUFBQUFBME9JeW1IcVhEaVlBQUFCZ0FsVk5ZMVRfWEFEUXRBdG1uLTlXQ0hnN2U5TExQUDJYYUNzTW13|d1aa7ab03e3c753f76a5697cb80e08da9d042a909458153bea0eadf0f3a665fa',
    'referer': 'https://www.zhihu.com/signup?next=%2F',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}


session = requests.Session()
source = session.get('https://zhihu.com', headers=header,verify=False).content.decode()
print(source)