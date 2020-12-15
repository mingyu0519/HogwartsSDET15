import datetime
import json
import pytest
import requests
from jsonpath import jsonpath
from testing.interface.tag import Tag


class TestTag:
    def setup_class(self):
        self.tag = Tag()

    # 增加标签-已有标签组
    @pytest.mark.parametrize("group_id, tag_name", [
        ['etEsuJCQAAckPHnumB9-Kyqrucop-sXQ', 'tag1_new_'],
        ['etEsuJCQAAckPHnumB9-Kyqrucop-sXQ', 'tag1——中文'],
        ['etEsuJCQAAckPHnumB9-Kyqrucop-sXQ', 'tag1[中文]']
    ])
    def test_tag_add(self, group_id, tag_name):
        tag_name = tag_name + str(datetime.datetime.now().strftime("%Y%m%d-%H%M%S"))
        r = self.tag.list()
        r = self.tag.add(
            group_id=group_id,
            tag_name=tag_name
        )
        r = self.tag.list()
        assert jsonpath(r.json(), f"$..[?(@.name=='{tag_name}')]")[0]['name'] == tag_name

    # 增加标签-无标签组
    @pytest.mark.parametrize("group_id, tag_name, group_name", [
        ['', 'tag1_new_', '测试标签组'],
        ['', 'tag1——中文', '测试标签组'],
        ['', 'tag1[中文]', '测试标签组']
    ])
    def test_tag_add_notag(self, group_id, tag_name, group_name):
        tag_name = tag_name + str(datetime.datetime.now().strftime("%Y%m%d-%H%M%S"))
        r = self.tag.list()
        r = self.tag.add(
            group_id=group_id,
            tag_name=tag_name,
            group_name=group_name
        )
        r = self.tag.list()
        assert jsonpath(r.json(), f"$..[?(@.name=='{tag_name}')]")[0]['name'] == tag_name

    # 删除标签
    def test_tag_del(self):
        r = self.tag.list()
        tag_ids = jsonpath(r.json(), f"$..tag_group[*].tag[*].id")
        if len(tag_ids) == 0:
            assert False, '当前没有可删除的标签'
        tag = tag_ids[0]
        r = self.tag.delete(
            tag_ids=[tag]
        )
        r = self.tag.list()
        assert tag not in jsonpath(r.json(), f"$..tag_group[*].tag[*].id")

    # 标签数据清理
    def test_tag_clean(self):
        r = self.tag.clear()
        assert r['tag_group'] == []