import datetime
import json

import requests


# todo: 与底层具体的实现框架代码耦合严重，无法适应变化，比如公司切换了协议，比如使用pb dubbo
# todo: 代码冗余，需要封装
# todo: 无法清晰的描述业务
# todo: 使用jsonpath表达更灵活的递归查找
def test_tag_list():
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
    print(token)

    r = requests.post(
        'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list',
        params={"access_token": token},
        json={
            'tag_id': []
        }
    )

    print(json.dumps(r.json(), indent=2))
    assert r.status_code == 200
    assert r.json()['errcode'] == 0

    tag_name = 'tag1_new_' + str(datetime.datetime.now().strftime("%Y%m%d-%H%M"))
    r = requests.post(
        'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/edit_corp_tag',
        params={"access_token": token},
        json={
            'id': 'etEsuJCQAAUNXLtKb7nXLC2GDZrVKuTg',
            'name': tag_name
        }
    )
    print(json.dumps(r.json(), indent=2))
    assert r.status_code == 200
    assert r.json()['errcode'] == 0

    r = requests.post(
        'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list',
        params={"access_token": token},
        json={
            'tag_id': []
        }
    )

    print(json.dumps(r.json(), indent=2))
    assert r.status_code == 200
    assert r.json()['errcode'] == 0
    tags = [
        tag
        for group in r.json()['tag_group'] if group['group_name'] == '\u6d4b\u8bd5\u6807\u7b7e'
        for tag in group['tag'] if tag['name'] == tag_name
    ]
    # jsonpath(f"$..[?(@.name='{tag_name}')]") jmepath
    assert tags != []