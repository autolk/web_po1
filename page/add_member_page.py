from page.contact_page import ContactPage
from base.Base import Base
from selenium.webdriver.common.by import By
class AddMemberPage(Base):

    _INPUY_USERNAME = (By.ID,'username')
    _INPUT_ACCID = (By.ID, 'memberAdd_acctid')
    _INPUT_PHONE = (By.ID, 'memberAdd_phone')
    _BTN_SAVE = (By.XPATH, '//*[text()="保存"]')

    def fill_info(self,name,accid,phone):
        self.driver.find_element(*self._INPUY_USERNAME).send_keys(name)
        self.driver.find_element(*self._INPUT_ACCID).send_keys(accid)
        self.driver.find_element(*self._INPUT_PHONE).send_keys(phone)
        self.driver.find_element(*self._BTN_SAVE).click()
        return ContactPage(self.driver)
