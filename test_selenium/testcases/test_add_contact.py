
from test_selenium.page.main_page import Main_Page


class TestAddContact:
    def setup_class(self):
        self.main = Main_Page()
    def test_addcontact(self):
        name_list = self.main.goto_add_contact_page().add_contactlist().check_memberlist()
        assert "张三1" in name_list