from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome('/Users/houzhimeng/Downloads/chromedriver')
driver.get('https://search.damai.cn/search.htm')


try:
    WebDriverWait(driver, 30).until(EC.text_to_be_present_in_element((By.CLASS_NAME, "content"), '通关'))
except Exception as _:
    print('网页加载太慢，不想等了。')

element = driver.find_element_by_xpath('//div[@class="content"]')
print(f'异步加载的内容是：{element.text}')

driver.quit()
