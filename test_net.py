#!/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

# 加载扩展
driver = webdriver.Chrome('/Users/houzhimeng/Downloads/chromedriver')
# profile.add_extension('/root/downloads/addon-328839-latest.xpi')
# profile.set_preference("extensions.y2bautohd.currentVersion", "49.1")
#
# driver = webdriver.chrome(firefox_profile=profile)

# 打开指定视频
driver.get('https://www.youtube.com/watch?v=TmDKbUrSYxQ')

# 切换标签页
driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.TAB)

# 刷新视频页
driver.get('https://www.youtube.com/watch?v=TmDKbUrSYxQ')
time.sleep(30)

# 点击右键
ele = driver.find_element_by_id('movie_player')
action_chains = ActionChains(driver)
action_chains.move_to_element_with_offset(ele, 100, 100).context_click().perform()
time.sleep(3)

# 点击详细统计信息
driver.find_element_by_xpath('//div[text() = "Stats for nerds"]').click()
time.sleep(3)

# 保存截图
img_name = str(time.time())[0:10] + '.png'
driver.save_screenshot('/Users/houzhimeng/Downloads/'+img_name)