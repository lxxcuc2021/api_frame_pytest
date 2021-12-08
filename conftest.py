#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/12/3 
# @Author : lixx
# @File : conftest.py
import pytest

from api_frame_pytest.common.yaml_util import YamlUtil

@pytest.fixture(scope='session', autouse=True)
def yaml_clear():
	"""
	清理yaml文件
	"""
	YamlUtil().clear_yaml()

# @pytest.fixture(scope='function')
# def conn_database():
# 	"""
# 	数据库连接
# 	"""
# 	print('连接数据库')
# 	yield
# 	print('断开数据库')
