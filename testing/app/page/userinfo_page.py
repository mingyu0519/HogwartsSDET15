from appium.webdriver.common.mobileby import MobileBy

from testing.app.page.deitcontact_page import Editpage
from testing.app.page.base_page import BasePage


class Userinfo(BasePage):
    def menu(self):
        self.find(MobileBy.XPATH,'//*[@text="个人信息"]/../../../../..//android.widget.RelativeLayout').click()
        return Editpage(self.driver)