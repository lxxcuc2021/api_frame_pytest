#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/12/7 
# @Author : lixx
# @File : request_util.py
import requests
import json

class RequestUtil:
	"""
	接口请求封装
	"""
	session = requests.session()

	def send_request(self, method, url, data, **kwargs):
		method = str(method).lower()
		if method == 'get':
			res = RequestUtil.session.request(method, url, params=data, **kwargs)
		else:
			data = json.dumps(data)
			res = RequestUtil.session.request(method, url, data=data, **kwargs)
		return res.text
