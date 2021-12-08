#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/12/3 
# @Author : lixx
# @File : yaml_util.py
import os
import yaml

class YamlUtil:
	"""
	yaml文件的读取和写入
	"""

	def read_yaml(self, key):
		"""
		yaml读取
		"""
		with open(os.getcwd()+'/../extract.yaml', 'r', encoding='utf-8') as f:
			value = yaml.load(stream=f, Loader=yaml.FullLoader)[key]
			return value

	def write_yaml(self, data):
		"""
		yaml写入
		"""
		with open(os.getcwd()+'/../extract.yaml', 'a', encoding='utf-8') as f:
			yaml.dump(data=data, stream=f, allow_unicode=True)

	def clear_yaml(self):
		with open(os.getcwd() + '/../extract.yaml', 'w', encoding='utf-8') as f:
			f.truncate()


	def read_request_yaml(self, yaml_name):
		"""
		yaml读取
		"""
		with open(os.getcwd()+'/testcase/'+yaml_name, 'r', encoding='utf-8') as f:
			value = yaml.load(stream=f, Loader=yaml.FullLoader)
			return value
