import pytest
import yaml

from test_selenium.page.main_page import Main_Page


class TestAddMember:
    def setup_class(self):
        self.main = Main_Page()


    def test_addmember(self):
        path = "../file/work_weixin.yml"
        with open(path, encoding='utf-8') as f:
            memberlists: list[dict] = yaml.safe_load(f)
            print(memberlists)
            for memberlist in memberlists:
                list_name = memberlist["name"]
                list_id = memberlist["id"]
                list_phone = memberlist["phone"]
                self.main.goto_addmember_page().add_member_list(list_name, list_id, list_phone)
        mem_list = self.main.goto_contact_page().check_memberlist()
        print(mem_list)
        for memberlist in memberlists:
            list_name = memberlist["name"]
            assert list_name in mem_list