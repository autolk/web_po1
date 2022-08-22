import time
# hahahhhh1111
#11

import yaml
from selenium import webdriver

class TestLogin():
    def test_login(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://work.weixin.qq.com/wework_admin/loginpage_wx?from=myhome_baidu')
        time.sleep(10)

        cookies = self.driver.get_cookies()
        with open('C:/Users/25238/Desktop/huo/web_po1/datas/cookies1.yaml','w')as f:
            yaml.safe_dump(data=cookies,stream=f)
            
