from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep

class TestWeChat:

    def setup(self):
        caps = {"platformName": "Android", "deviceName": "hogwarts", "appPackage": "com.tencent.wework",
                "appActivity": ".launch.LaunchSplashActivity", "noReset": "True"}
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(5)

    def test_wechat(self):
        self.driver.find_element(MobileBy.XPATH, "//*[@text='工作台']").click()
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector()\
                                 .scrollable(true).instance(0))\
                                 .scrollIntoView(new UiSelector()\
                                 .text("打卡").instance(0));').click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='外出打卡']").click()
        self.driver.find_element(MobileBy.XPATH, '//*[contains(@text,"次外出")]').click()
        assert "外出打卡成功" in self.driver.page_source

    def teardown(self):
        self.driver.quit()