import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


def muliti_click(button_element, until_ele):
    # 函数封装，这些代码逻辑要结合源码进行看
    # 解决的问题：有的按钮点击一次没有反应，可能要点击多次
    # 解决的方案：一直点击按钮，直到下个页面出现，封装成显式等待的一个条件
    # 在限制时间内会一直点击按钮，直到展示弹框
    def inner(driver):
        # 封装点击方法
        driver.find_element(By.XPATH, button_element).click()
        return driver.find_element(By.XPATH, until_ele)

    return inner

def click():

    driver = webdriver.Chrome()

    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get("https://vip.ceshiren.com/#/ui_study")

    WebDriverWait(driver,1000).until(muliti_click("//*[text()='点击两次响应']","//*[text()='该弹框点击两次后才会弹出']"))
    time.sleep(5)

if __name__ == '__main__':
    click()
