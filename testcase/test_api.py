#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/12/3
# @Author : lixx
# @File : test_api.py
import requests
import pytest
import json
from api_frame_pytest.common.request_util import RequestUtil
from api_frame_pytest.common.yaml_util import YamlUtil
import random


class TestAPI:
    """
    测试微信公众平台接口
    """
    # 数据驱动，读取yaml文件中的测试数据
    @pytest.mark.parametrize('caseinfo', YamlUtil().read_request_yaml('get_token.yaml'))
    def test_get_token(self, caseinfo):
        """
        获取access_token
        """
        # url = "https://api.weixin.qq.com/cgi-bin/token"
        # data = {
        #     "grant_type": "client_credential",
        #     "appid": "wxa6a4bba2f6d77b05",
        #     "secret": "98e2a38d704c38b6888218620b1f8ed4"
        # }
        method = caseinfo['request']['method']
        url = caseinfo['request']['url']
        data = caseinfo['request']['data']
        res = RequestUtil().send_request(method, url, data)
        res = json.loads(res)  # 文本格式转换为json格式
        token = res['access_token']
        YamlUtil().write_yaml({'token': token})  # 将token写入yaml文件，接口关联
        assert 'access_token' in res

    # 用户标签管理
    def test_add_tag(self):
        token = YamlUtil().read_yaml('token')
        url = "https://api.weixin.qq.com/cgi-bin/tags/create?access_token="+token
        tag = "tag_"+str(random.randint(0, 99999))
        data = {"tag":
                    {"name": tag}
        }
        res = requests.post(url=url, json=data)
        print(res.json())
        assert res.json()['tag']['name'] == tag
