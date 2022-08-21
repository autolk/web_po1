from page.add_member_page import AddMemberPage
from base.Base import Base
from selenium.webdriver.common.by import By
class HomePage(Base):
    _BTN_ADD = (By.CSS_SELECTOR,".index_service_cnt_item_title")

    def click_add(self):
        # self.driver.find_element_by_id()
        # self.driver.find_element(*self._BTN_ADD).click()
        self.find_and_click(*self._BTN_ADD)
        return AddMemberPage(self.driver)