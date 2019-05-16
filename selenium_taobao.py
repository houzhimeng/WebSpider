from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome('/Users/houzhimeng/Downloads/chromedriver')
driver.get('http://www.taobao.com')

input_frist = driver.find_element_by_id('q')
input_send = input_frist.send_keys('hahaha')
button = input_frist.find_element_by_class_name('btn-search')
button.click()