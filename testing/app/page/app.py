import yaml
from appium import webdriver
from testing.app.page.main_page import  MainPage
from testing.app.page.base_page import BasePage

with open('caps.yml') as f:
    conf = yaml.safe_load(f)
    caps = conf['caps']


class App(BasePage):

    def __init__(self):
        self.driver = webdriver.Remote(f"http://localhost:4273/wd/hub", caps)

    def start(self):
        if self.driver is None:
            self.driver.implicitly_wait(5)
        else:
            self.driver.launch_app()
        return self

    def restart(self):
        self.driver.close_app()
        self.driver.launch_app()
        pass

    def stop(self):
        self.driver.quit()

    def goto_main(self)->MainPage:
        return MainPage(self.driver)