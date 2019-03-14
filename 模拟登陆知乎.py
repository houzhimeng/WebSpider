from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome('/Users/houzhimeng/Downloads/chromedriver') #填写你的chromedriver的路径
driver.get("https://www.zhihu.com/signup?next=%2F")

elem = driver.find_element_by_name("username") #寻找账号输入框
elem.clear()
elem.send_keys("18611720843") #输入账号
password = driver.find_element_by_name('password') #寻找密码输入框
password.clear()
password.send_keys("Hzm885649") #输入密码

input('请在网页上点击倒立的文字，完成以后回到这里按任意键继续。')
elem.send_keys(Keys.RETURN) #模拟键盘回车键
time.sleep(10) #这里可以直接sleep, 也可以使用上一章讲到的等待某个条件出现
print(driver.page_source)
driver.quit()





cookie: _zap=48356585-ec48-411b-9a66-d487b7ae607b; d_c0="ANDiMph6lw6PTvEQHMMifR0QmejqXGqazZ8=|1543463744"; l_cap_id="MjRjNWNkZDA1YWQ4NDY4MjkxMGRhYzc2OTkyNWZiNDI=|1544601803|6786e6673fe0f040c6a9223f5f4baed9721dc814"; r_cap_id="YmE5MzhmZTIyZTEzNDRmZmE2OTQwZWZjNDRjODNlNDE=|1544601803|815c2e4c7621df052c4f61ed8bfc68b51b758acd"; cap_id="MzM5MzBhMzA5ZGQ0NDkwNTg5MjFjNjkwNDgxZjM0MzA=|1544601803|6cfb19bf6f9133eff82dea3b17141cc2276e9a73"; _xsrf=h29qRM08rAMJXER3FsTSUGeR67a9bAAd; tst=r; tgw_l7_route=931b604f0432b1e60014973b6cd4c7bc; capsion_ticket="2|1:0|10:1544685115|14:capsion_ticket|44:MWNiNmVhNzc4NzUzNDJhNDhlZjgyNzk0NjRjMTk1YWM=|727a2ae3d07f83ff43bdceeeef8990f2dc9d0442e52ae6a04b8702f38c716be5"; z_c0="2|1:0|10:1544685155|4:z_c0|92:Mi4xSkxzaEFnQUFBQUFBME9JeW1IcVhEaVlBQUFCZ0FsVk5ZMVRfWEFEUXRBdG1uLTlXQ0hnN2U5TExQUDJYYUNzTW13|d1aa7ab03e3c753f76a5697cb80e08da9d042a909458153bea0eadf0f3a665fa"
