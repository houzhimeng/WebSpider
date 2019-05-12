from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome('/Users/houzhimeng/Downloads/chromedriver')
# driver.get("https://www.ttplus.cn/day.html")
# driver.find_element_by_link_text(u"图集").click()
# driver.find_element_by_link_text(u"体坛周报").click()
# driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='搜索'])[1]/following::img[1]").click()
# driver.find_element_by_xpath("xpath=(.//*[normalize-space(text()) and normalize-space(.)='搜索'])[1]/following::img[1]").click()
# html = driver.page_source
# print(html)


driver.get("http://bbs.a9vg.com/forum.php")
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "myDynamicElement"))
    )
finally:
    driver.quit()
driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='密码'])[1]/following::em[1]").click()
driver.find_element_by_id("w_username").click()