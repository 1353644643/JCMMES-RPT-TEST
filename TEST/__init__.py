from selenium import webdriver
import time
wd=webdriver.Firefox()
wd.get('http://localhost:9201/Account/Login?ReturnUrl=%2Foauth%2Fauthorize%3Fredirect_url%3Dhttp%3A%2F%2Flocalhost%3A9200%2F%26client_id%3DXCSmart%26response_type%3Dcode%26direct%3Dtrue')
time.sleep(0)
wd.maximize_window()
#登陆

wd.find_element_by_xpath('/html/body/div[3]/form/div[1]/input').send_keys('admin')
wd.find_element_by_xpath('/html/body/div[3]/form/div[2]/input').send_keys('123qwe')
wd.find_element_by_xpath('/html/body/div[3]/form/div[3]/button').click()
time.sleep(3)

wd.find_element_by_xpath("//input[@id='kw']").send_keys(123)
time.sleep(2)
wd.find_element_by_xpath("//input[@type='submit']").click()































