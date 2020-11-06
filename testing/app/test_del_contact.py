from testing.app.page.app import App


class TestDelContact:
    def setup(self):
        self.app = App()
        self.main = self.app.start().goto_main()

    def test_del_contact(self):
        name = '小明同学'
        result = self.main.goto_address().click_contact_manager().click_contact_delete(name).delete_member().close_contact().search_contact(name)
        assert '无搜索结果' == result

    def teardown(self):
        self.app.stop()
