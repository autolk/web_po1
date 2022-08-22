from selenium import webdriver
import yaml
from page.home_page import HomePage
from base.Base import Base
import time
class LoginPage(Base):

    def login(self):

        with open('C:/Users/25238/Desktop/huo/web_po1/datas/cookies1.yaml','r')as f:
            cookies = yaml.safe_load(f)

        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.get('https://work.weixin.qq.com/wework_admin/loginpage_wx?from=myhome_baidu')
        time.sleep(25)
        return HomePage(self.driver)


