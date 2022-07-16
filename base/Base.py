from selenium import webdriver

class Base():
    def __init__(self,base_driver=None):

        if base_driver == None:
            self.driver = webdriver.Chrome()
            self.driver.get('https://work.weixin.qq.com/wework_admin/loginpage_wx?from=myhome_baidu')
            self.driver.maximize_window()
            self.driver.implicitly_wait(5)
        else:
            self.driver = base_driver

