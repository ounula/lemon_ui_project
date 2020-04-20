# -*- encoding:utf-8 -*-
# @Time : 2020/4/16 17:15 
# @Author : ZHH
from selenium import webdriver
from PageObjects.ptsdList_p import PtsdList
from PageObjects.createPtsd_p import CreatePtsd
from TestDatas import common_datas as CD
from TestDatas import login_datas as LD
from Common.logger import Log
from PageObjects.login_p import LoginPage
import pytest


@pytest.mark.usefixtures("login_success")
@pytest.mark.usefixtures("back_page")
class TestPtsdPage:
    def test_clickNewPtsd(self,login_success):
        Log().log_info("**********普通送达列表：正常场景   -   点击新建普通送达打开对应页面**********")
        PtsdList(login_success).new_ptsd()
        assert CreatePtsd(login_success).is_Exist_baseinfo()

    def test_