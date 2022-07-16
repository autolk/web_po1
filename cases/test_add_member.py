from page.login_page import LoginPage


class TestAddMember():
    # def setupclass(self):
    #     self.home = LoginPage().login()

    def setup(self):
        from faker import Faker
        fake = Faker('zh_CN')
        self.name = fake.name()
        self.phone_number = fake.phone_number()
        self.accid = fake.ssn()

    def test_add_member(self):
        text = LoginPage().login().click_add().fill_info(self.name,self.accid,self.phone_number).get_tip()
        print(text)
        assert text == '保存成功'




