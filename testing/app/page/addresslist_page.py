from testing.app.page.base_page import BasePage
from testing.app.page.member_invite_menu_page import MemberInviteMenuPage
from appium.webdriver.common.mobileby import MobileBy


class AddressListPage(BasePage):

    def click_contact(self):
        self.find_by_scroll("添加成员").click()
        return MemberInviteMenuPage(self.driver)

    def click_contact_manager(self):
        self.find_and_click(MobileBy.ID, 'com.tencent.wework:id/hxr')
        return self

    def click_contact_delete(self, name):
        self.wait_click(15, MobileBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector()'
                                                          '.scrollable(true).instance(0))'
                                                          f'.scrollIntoView(new UiSelector().textContains("{name}")'
                                                          '.instance(0));')

        self.find_and_click(MobileBy.XPATH, f'//*[@text="{name}"]')

        from testing.app.page.contactedit_page import Editpage
        return Editpage(self.driver)

    def close_contact(self):
        self.wait_click(15, MobileBy.ID, 'com.tencent.wework:id/hxm')
        return self

    def search_contact(self, name):
        self.find_and_click(MobileBy.ID, 'com.tencent.wework:id/hxw')
        self.find_and_sendkeys(MobileBy.ID, 'com.tencent.wework:id/ghu', name)
        return self.find(MobileBy.ID, 'com.tencent.wework:id/ca0').text