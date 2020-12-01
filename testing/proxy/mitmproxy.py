import json

from mitmproxy import http


def response(flow: http.HTTPFlow):
    # 加上过滤条件
    if "quote.json" in flow.request.pretty_url and "x=" in flow.request.pretty_url:
        # 把响应数据转化成python对象，保存到data中
        data = json.loads(flow.response.content)
        # 第一支股票的名称不变
        data['data']['items'][0]['quote']['name'] = data['data']['items'][0]['quote']['name']
        # 第二支股票的名称加长一倍
        data['data']['items'][1]['quote']['name'] = data['data']['items'][1]['quote']['name'] * 2
        # 第三支股票的名称为空
        data['data']['items'][2]['quote']['name'] = ""
        # 把修改后的内容赋值给 response 原始数据格式
        flow.response.text = json.dumps(data)
