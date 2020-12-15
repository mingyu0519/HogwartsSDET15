import datetime
import json

import requests
from jsonpath import jsonpath


class Tag:

    def __init__(self):
        self.token = self.get_token()

    def get_token(self):
        corpid = 'wxaa6e18ac7322dc08'
        corpsecret = 'ocT0EkmYXREQb95tplpoApxy73yDul87yPKt8ra0Za4'

        r = requests.get(
            'https://qyapi.weixin.qq.com/cgi-bin/gettoken',
            params={'corpid': corpid, 'corpsecret': corpsecret}

        )
        print(json.dumps(r.json(), indent=2))
        assert r.status_code == 200
        assert r.json()['errcode'] == 0

        token = r.json()['access_token']
        return token

    def add(self, group_id, tag_name, group_name):
        data = {
                "tag": [{
                    "name": tag_name
                }
                ]
            }
        if group_id != '':
            data['group_id'] = group_id
        if group_name != '':
            data['group_name'] = group_name
        r = requests.post(
            'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag',
            params={"access_token": self.token},
            json=data
        )

        print(json.dumps(r.json(), indent=2))
        return r

    def list(self):
        r = requests.post(
            'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list',
            params={"access_token": self.token},
            json={
                'tag_id': []
            }
        )

        print(json.dumps(r.json(), indent=2))
        return r

    def update(self, id, tag_name):
        r = requests.post(
            'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/edit_corp_tag',
            params={"access_token": self.token},
            json={
                'id': id,
                'name': tag_name
            }
        )
        print(json.dumps(r.json(), indent=2))
        return r

    def delete(self, tag_ids, group_ids=[]):
        r = requests.post(
            'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag',
            params={"access_token": self.token},
            json={
                "tag_id": tag_ids,
                "group_id": group_ids
            }
        )
        print(json.dumps(r.json(), indent=2))
        return r

    def clear(self):
        r = self.list()
        group_ids = jsonpath(r.json(), f"$..tag_group[*].group_id")
        tag_ids = jsonpath(r.json(), f"$..tag_group[*].tag[*].id")
        self.delete(tag_ids, group_ids)
        r = self.list()
        return r