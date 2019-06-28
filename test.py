"""from selenium import webdriver
import time
wd=webdriver.Chrome()
wd.get('http://localhost:9201/Account/Login?ReturnUrl=%2Foauth%2Fauthorize%3Fredirect_url%3Dhttp%3A%2F%2Flocalhost%3A9200%2F%26client_id%3DXCSmart%26response_type%3Dcode%26direct%3Dtrue')
time.sleep(1)
wd.maximize_window()
#登陆
wd.find_element_by_xpath('/html/body/div[3]/form/div[1]/input').send_keys('admin')
wd.find_element_by_xpath('/html/body/div[3]/form/div[2]/input').send_keys('123qwe')
wd.find_element_by_xpath('/html/body/div[3]/form/div[3]/button').click()
time.sleep(3)
"""
import testdata
import  random

class Users(testdata.DictFactory):
    id = testdata.CountingFactory(10)
    name = testdata.FakeDataFactory('name')
    address = testdata.FakeDataFactory('address')
    age = testdata.RandomInteger(10, 30)
    gender = testdata.RandomSelection(['female', 'male'])
for user in Users().generate(10): # let say we only want 10 users
    print (user)











































wd.quit()