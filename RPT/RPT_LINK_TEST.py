from selenium import webdriver
import time
wd=webdriver.Chrome()
wd.get('http://localhost:9201/Account/Login?ReturnUrl=%2Foauth%2Fauthorize%3Fredirect_url%3Dhttp%3A%2F%2Flocalhost%3A9200%2F%26client_id%3DXCSmart%26response_type%3Dcode%26direct%3Dtrue')
time.sleep(3)
wd.maximize_window()
#登陆
wd.find_element_by_xpath('/html/body/div[3]/form/div[1]/input').send_keys('admin')
wd.find_element_by_xpath('/html/body/div[3]/form/div[2]/input').send_keys('123qwe')
wd.find_element_by_xpath('/html/body/div[3]/form/div[3]/button').click()
time.sleep(3)

# 在制品数据报表 -- 链接测试


wd.find_element_by_xpath('/html/body/app-root/layout-default/layout-sidebar/div/sidebar-nav/ul/li[8]/a/span').click()
time.sleep(2)
wd.find_element_by_xpath('/html/body/app-root/layout-default/layout-sidebar/div/sidebar-nav/ul/li[8]/ul/li[1]/a').click()
time.sleep(3)
wd.find_element_by_xpath('/html/body/app-root/layout-default/layout-sidebar/div/sidebar-nav/ul/li[8]/ul/li[2]/a').click()
time.sleep(3)
wd.find_element_by_xpath('/html/body/app-root/layout-default/layout-sidebar/div/sidebar-nav/ul/li[8]/ul/li[3]/a').click()
time.sleep(3)
wd.find_element_by_xpath('/html/body/app-root/layout-default/layout-sidebar/div/sidebar-nav/ul/li[8]/ul/li[4]/a').click()
time.sleep(3)
wd.find_element_by_xpath('/html/body/app-root/layout-default/layout-sidebar/div/sidebar-nav/ul/li[8]/ul/li[5]/a').click()
time.sleep(3)
wd.find_element_by_xpath('/html/body/app-root/layout-default/layout-sidebar/div/sidebar-nav/ul/li[8]/ul/li[6]/a').click()
time.sleep(3)
wd.find_element_by_xpath('/html/body/app-root/layout-default/layout-sidebar/div/sidebar-nav/ul/li[8]/ul/li[7]/a').click()
time.sleep(3)


# 测试类数据报表  -- 链接测试

wd.find_element_by_xpath('/html/body/app-root/layout-default/layout-sidebar/div/sidebar-nav/ul/li[9]/a/span').click()
time.sleep(2)
wd.find_element_by_xpath('/html/body/app-root/layout-default/layout-sidebar/div/sidebar-nav/ul/li[9]/ul/li[1]/a').click()
time.sleep(3)
wd.find_element_by_xpath('/html/body/app-root/layout-default/layout-sidebar/div/sidebar-nav/ul/li[9]/ul/li[2]/a').click()
time.sleep(3)
wd.find_element_by_xpath('/html/body/app-root/layout-default/layout-sidebar/div/sidebar-nav/ul/li[9]/ul/li[3]/a').click()
time.sleep(3)
wd.find_element_by_xpath('/html/body/app-root/layout-default/layout-sidebar/div/sidebar-nav/ul/li[9]/ul/li[4]/a').click()
time.sleep(3)
wd.find_element_by_xpath('/html/body/app-root/layout-default/layout-sidebar/div/sidebar-nav/ul/li[9]/ul/li[5]/a').click()
time.sleep(3)

#统计类数据报表--链接测试
wd.find_element_by_xpath('/html/body/app-root/layout-default/layout-sidebar/div/sidebar-nav/ul/li[10]/a/span').click()
time.sleep(1)
wd.find_element_by_xpath('/html/body/app-root/layout-default/layout-sidebar/div/sidebar-nav/ul/li[10]/ul/li[1]/a').click()
time.sleep(3)
wd.find_element_by_xpath('/html/body/app-root/layout-default/layout-sidebar/div/sidebar-nav/ul/li[10]/ul/li[2]/a').click()
time.sleep(3)
wd.find_element_by_xpath('/html/body/app-root/layout-default/layout-sidebar/div/sidebar-nav/ul/li[10]/ul/li[3]/a').click()
time.sleep(3)
wd.find_element_by_xpath('/html/body/app-root/layout-default/layout-sidebar/div/sidebar-nav/ul/li[10]/ul/li[4]/a').click()
time.sleep(3)
wd.find_element_by_xpath('/html/body/app-root/layout-default/layout-sidebar/div/sidebar-nav/ul/li[10]/ul/li[5]/a').click()
time.sleep(3)
wd.find_element_by_xpath('/html/body/app-root/layout-default/layout-sidebar/div/sidebar-nav/ul/li[10]/ul/li[6]/a').click()
time.sleep(3)
wd.find_element_by_xpath('/html/body/app-root/layout-default/layout-sidebar/div/sidebar-nav/ul/li[10]/ul/li[7]/a').click()
time.sleep(3)
wd.find_element_by_xpath('/html/body/app-root/layout-default/layout-sidebar/div/sidebar-nav/ul/li[10]/ul/li[8]/a').click()
time.sleep(3)
#设备数据报表--链接测试
wd.find_element_by_xpath('/html/body/app-root/layout-default/layout-sidebar/div/sidebar-nav/ul/li[11]/a/span').click()
time.sleep(2)
wd.find_element_by_xpath('/html/body/app-root/layout-default/layout-sidebar/div/sidebar-nav/ul/li[11]/ul/li[1]/a').click()
time.sleep(3)
wd.find_element_by_xpath('/html/body/app-root/layout-default/layout-sidebar/div/sidebar-nav/ul/li[11]/ul/li[2]/a').click()
time.sleep(3)
wd.find_element_by_xpath('/html/body/app-root/layout-default/layout-sidebar/div/sidebar-nav/ul/li[11]/ul/li[3]/a').click()
time.sleep(3)



wd.quit()


















































