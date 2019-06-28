from selenium import webdriver
import time
wd=webdriver.Chrome()
wd.get('http://localhost:9201/Account/Login?ReturnUrl=%2Foauth%2Fauthorize%3Fredirect_url%3Dhttp%3A%2F%2Flocalhost%3A9200%2F%26client_id%3DXCSmart%26response_type%3Dcode%26direct%3Dtrue')
time.sleep(0)
wd.maximize_window()
#登陆
wd.find_element_by_xpath('/html/body/div[3]/form/div[1]/input').send_keys('admin')
wd.find_element_by_xpath('/html/body/div[3]/form/div[2]/input').send_keys('123qwe')
wd.find_element_by_xpath('/html/body/div[3]/form/div[3]/button').click()
time.sleep(1)
# 验证 ‘在制品数据报表--在制品数据’ 查询功能
# wd.find_element_by_xpath("/html/body/app-root/layout-default/layout-sidebar/div/sidebar-nav/ul/li[8]/a/span").click()
# time.sleep(3)
wd.find_element_by_xpath("/html/body/app-root/layout-default/layout-sidebar/div/sidebar-nav/ul/li[8]/a/span").click()
time.sleep(3)
wd.find_element_by_xpath("//a[@class='sidebar-nav__item-link ng-star-inserted']").click()
time.sleep(2)




wd.quit()














































wd.quit()