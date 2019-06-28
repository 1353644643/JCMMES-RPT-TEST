from selenium import webdriver
import time
wd=webdriver.Chrome()
wd.get('http://www.baidu.com')
time.sleep(0)
wd.maximize_window()
#登陆
"""
wd.find_element_by_xpath('/html/body/div[3]/form/div[1]/input').send_keys('admin')
wd.find_element_by_xpath('/html/body/div[3]/form/div[2]/input').send_keys('123qwe')
wd.find_element_by_xpath('/html/body/div[3]/form/div[3]/button').click()
time.sleep(1)
"""
wd.find_element_by_xpath("//input[@id='kw']").send_keys(123)
wd.find_element_by_xpath("//input[@type='submit']").click()
# wd.find_element_by_xpath('/html/body/div[3]/form/div[3]/button').click()






























