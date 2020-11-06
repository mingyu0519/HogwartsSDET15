from testing.app.page.contactdel_page import Delete_page
from testing.app.page.base_page import BasePage
from appium.webdriver.common.mobileby import MobileBy

class Editpage(BasePage):
    def edit_member(self):
        self.find(MobileBy.XPATH,'//*[@text="编辑成员"]').click()
        return Delete_page(self.driver)