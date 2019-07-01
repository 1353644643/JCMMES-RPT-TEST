from selenium import webdriver
import time
wd=webdriver.Firefox()
wd.get('http://www.baidu.com')
time.sleep(1)
wd.maximize_window()


def  picture_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    print(picture_time)
    try:
        picture_url=wd.get_screenshot_as_file('E:\\git\\JCMMES-RPT-TEST\\image\\'+ picture_time +'.png')
        print("%s：截图成功！！！" % picture_url)
except BaseException as msg:
    print(msg)
