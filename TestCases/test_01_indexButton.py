# -*- encoding:utf-8 -*-
# @Time : 2020/4/16 17:34 
# @Author : ZHH
from selenium import webdriver
from PageObjects.login_p import LoginPage
from PageObjects.index_p import IndexPage
from TestDatas import common_datas as CD
from TestDatas import login_datas as LD
from Common.logger import Log
import pytest

@pytest.mark.usefixtures("loggin_success")
class TestIndexPage:
    Log().log_info('====================主页菜单、登出=====================')