from base.Base import Base
from selenium.webdriver.common.by import By
# js_tips
class ContactPage(Base):
    _TIPS = (By.ID,'js_tips')
    def get_tip(self):
        # result = self.driver.find_element(*self._TIPS).text
        result = self.find_and_text(*self._TIPS)
        return result