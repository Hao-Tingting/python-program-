
from test_selenium.page.main_page import Main_Page


class TestAddDepart:
    def setup_class(self):
        self.main = Main_Page()
    def test_adddepart(self):
        depart_list = self.main.goto_contact_page().goto_add_depart().add_departlist()
        assert "人事部" in depart_list