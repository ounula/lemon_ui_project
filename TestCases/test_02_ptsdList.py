# -*- encoding:utf-8 -*-
# @Time : 2020/4/16 17:15 
# @Author : ZHH
from selenium import webdriver
from PageObjects.ptsdList_p import PtsdList
from TestDatas import common_datas as CD
from TestDatas import login_datas as LD
from Common.logger import Log
import pytest

@pytest.mark.usefixtures("loggin_success")
class TestPtsdPage:
    Log().log_info('====================普通送达=====================')

    # @pytest.mark.usefixtures("back_page")
    # def test_clickNewPtsd(self):
