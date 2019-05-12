from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
#
# driver = webdriver.Chrome('/Users/houzhimeng/Downloads/chromedriver')
# driver.get('https://baidu.com')
#
#
# # try:
# #     WebDriverWait(driver, 30).until(EC.text_to_be_present_in_element((By.CLASS_NAME, "content"), '通过'))
# # except Exception as _:
# #     print('网页加载太慢，不想等了。')
#
# #查找对象
# # driver.find_element_by_id("su").click()
#
# #元素定位
# driver.find_element_by_id("kw").send_keys("ljiushiwo")
# driver.find_element_by_id("su").click()
#
#
#
# # driver.quit()


# coding=utf-8
# from selenium import webdriver
# import time

#实例化一个浏览器
driver = webdriver.Chrome('/Users/houzhimeng/Downloads/chromedriver')
# driver = webdriver.PhantomJS()

#设置窗口大小
# driver.set_window_size(1920,1080)

#最大化窗口
driver.maximize_window()

#发送请求
driver.get("http://www.baidu.com")

#进行页面截屏
driver.save_screenshot("./baidu.png")

#元素定位的方法
driver.find_element_by_id("kw").send_keys("python")
driver.find_element_by_id("su").click()

# driver 获取html字符串
# print(driver.page_source) #浏览器中elements的内容

print(driver.current_url)

#driver获取cookie
# cookies = driver.get_cookies()
# print(cookies)
# print("*"*100)
# cookies = {i["name"]:i["value"] for i in cookies}
# print(cookies)

#退出浏览器
time.sleep(3)
driver.quit()
