from appium.webdriver.common.mobileby import MobileBy

from testing.app.page.addresslist_page import AddressListPage
from testing.app.page.base_page import BasePage


class MainPage(BasePage):
    address_element = (MobileBy.XPATH, "//*[@text='通讯录']")

    def goto_address(self):
        self.find_and_click(*self.address_element)
        return AddressListPage(self.driver)
