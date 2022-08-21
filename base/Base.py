from selenium import webdriver
from base.base_handle import black_wrapper
import time
class Base():
    def __init__(self,base_driver=None):

        if base_driver == None:
            self.driver = webdriver.Chrome()
            self.driver.get('https://work.weixin.qq.com/wework_admin/loginpage_wx?from=myhome_baidu')
            self.driver.maximize_window()
            self.driver.implicitly_wait(5)
        else:
            self.driver = base_driver

    def get_time(self):
        t = time.localtime(time.time())
        cur_time = time.strftime("%Y-%m-%d_%H_%M_%S", t)
        print("当前时间为：{cur_time}")
        return cur_time

    @black_wrapper
    def find(self, by, locator):
        return self.driver.find_element(by, locator)

    def find_and_click(self, by, locator):
        self.find(by, locator).click()

    def find_and_send(self, by, locator, text):
        self.find(by, locator).send_keys(text)
