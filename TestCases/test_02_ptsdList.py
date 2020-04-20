# -*- encoding:utf-8 -*-
# @Time : 2020/4/16 17:15 
# @Author : ZHH
from selenium import webdriver
from PageObjects.ptsdList_p import PtsdList
from TestCases.test_00_login import TestLogin
from PageObjects.createPtsd_p import CreatePtsd
from TestDatas import common_datas as CD
from TestDatas import login_datas as LD
from Common.logger import Log
import pytest


@pytest.mark.usefixtures("access_web")
@pytest.mark.usefixtures("back_page")
class TestPtsdPage:
    def test_clickNewPtsd(self, access_web):
        Log().log_info("**********普通送达列表：正常场景   -   点击新建普通送达打开对应页面**********")
        TestLogin().test_login_success(access_web)
        PtsdList(access_web[0]).new_ptsd()
