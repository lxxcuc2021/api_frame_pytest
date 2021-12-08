#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021/12/3 
# @Author : lixx
# @File : all.py
import pytest
import os
if __name__ == '__main__':
	pytest.main()
	os.system('allure generate temp -o report --clean')