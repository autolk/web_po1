from selenium import webdriver
import yaml
from page.home_page import HomePage
from base.Base import Base
class LoginPage(Base):

    def login(self):

        with open('./datas/cookies.yaml','r')as f:
            cookies = yaml.safe_load(f)

        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.get('https://work.weixin.qq.com/wework_admin/loginpage_wx?from=myhome_baidu')

        return HomePage(self.driver)

# LoginPage().login()
