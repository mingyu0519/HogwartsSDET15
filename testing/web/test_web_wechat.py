#!/usr/bin/env python
# -*- coding: utf-8 -*-
import shelve
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TestWebWechat():

    def setup(self):
        options = Options()
        options.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=options)

    def test_cookie(self):
        cookies = [{'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False, 'value': '1688853723289782'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False, 'value': 'o8c7fH473J1LiAuDFYU_xmKC5O_xd3vfedOpXjjajxisKjpa9zWtoaqkoyargrRkstJTGG1tNk3WkeOkNuWNnD_moE5eIoYBMcZAvVhHhWdJMtD-8Svt0tedZzg-0Txe_YurCtg56oiwxsthNlB-AJzqjQ3O6V7qDm3NGdJB3RGjy0jWxGXyLlAjm3Z4aHbIQGGiEg7y5qQ71uPue97N59QrwLHl8MElBKykRGmhe_I7cPUknCb8Vhr3JwHB9DNtYuAeKYdYPCZQWxqK5kK21Q'}, {'domain': '.qq.com', 'expiry': 2235123296, 'httpOnly': False, 'name': 'pac_uid', 'path': '/', 'secure': True, 'value': '1_769456011'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False, 'value': '1970324996999954'}, {'domain': '.qq.com', 'expiry': 2235123296, 'httpOnly': False, 'name': 'pgv_pvi', 'path': '/', 'secure': True, 'value': '1525084160'}, {'domain': '.qq.com', 'expiry': 2235123296, 'httpOnly': False, 'name': 'o_cookie', 'path': '/', 'secure': True, 'value': '769456011'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False, 'value': 'a6970920'}, {'domain': '.qq.com', 'expiry': 2235123296, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': True, 'value': 'CEyBbrcDTD'}, {'domain': '.qq.com', 'expiry': 2235123296, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': True, 'value': '77601a00064525e8f2062ac139560efaf64009fb90eaf6b3f3c4a2cdffea8377'}, {'domain': '.work.weixin.qq.com', 'expiry': 1606995426.977474, 'httpOnly': False, 'name': 'wwrtx.i18n_lan', 'path': '/', 'secure': False, 'value': 'zh'}, {'domain': '.qq.com', 'expiry': 1667475420, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False, 'value': 'GA1.2.1977516214.1603372512'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False, 'value': 'dz0a1DweS-GMYwOj5C5v_biukBZ4IzdBBTWlfnwAqc_lFuaN2cI1CXCJVjpi6-gJ'}, {'domain': '.qq.com', 'expiry': 1604489820, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False, 'value': 'GA1.2.1538994000.1604403297'}, {'domain': '.qq.com', 'expiry': 1915686782.345934, 'httpOnly': False, 'name': 'iip', 'path': '/', 'secure': False, 'value': '0'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.work.weixin.qq.com', 'expiry': 2235123296, 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': True, 'value': 'direct'}, {'domain': '.qq.com', 'expiry': 2235123296, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/', 'secure': True, 'value': '9783778175'}, {'domain': '.work.weixin.qq.com', 'expiry': 2235123296, 'httpOnly': False, 'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': True, 'value': '1603354466'}, {'domain': '.work.weixin.qq.com', 'expiry': 2235123296, 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': True, 'value': '22815482122970383'}, {'domain': '.work.weixin.qq.com', 'expiry': 2235123296, 'httpOnly': False, 'name': 'wwrtx.c_gdpr', 'path': '/', 'secure': True, 'value': '0'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False, 'value': '1688853723289782'}, {'domain': '.work.weixin.qq.com', 'expiry': 2235123296, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/', 'secure': True, 'value': '3ih62r4'}, {'domain': 'work.weixin.qq.com', 'expiry': 2235123296, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/', 'secure': True, 'value': '3ih62r4'}, {'domain': '.qq.com', 'expiry': 2235123296, 'httpOnly': False, 'name': 'tvfe_boss_uuid', 'path': '/', 'secure': True, 'value': '55ab945dda1ebe75'}]
        db = shelve.open("cookies")
        db['cookie'] = cookies
        cookies = db['cookie']
        db.close()

        # 利用读取的cookie 完成登录操作
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        for cookie in cookies:
            if 'expiry' in cookie.keys():
                cookie.pop('expiry')
            self.driver.add_cookie(cookie)

        self.driver.refresh()
        time.sleep(3)
        # 查找"导入通讯录"按钮
        self.driver.find_element(By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(2)").click()
        time.sleep(3)
        # 上传通讯录文件
        self.driver.find_element(By.CSS_SELECTOR, '.ww_fileImporter_fileContainer_uploadInputMask').send_keys("/Users/wangmingyu/Downloads/Contacts.xlsx")
        # 验证文件名称
        name = self.driver.find_element(By.CSS_SELECTOR, '.ww_fileImporter_fileContainer_fileNames').text
        assert "Contacts.xlsx" == name

    def teardown(self):
        self.driver.quit()
