# -*- coding: UTF-8 –*-
#author: zhh
#time: 2020/4/12 19:29
import unittest
from PageObjects.login_p import LoginPage
from PageObjects.index_p import IndexPage
from TestDatas import login_datas as LD
import ddt
#正常用例
#前提：
#1、用户已登录
# 2、有能够投资的标     如果没有，先加标
# 3、用户有余额可以投标

class TestInvest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("==========开始测试投标模块==========")
    def setUp(self) -> None:
        pass
    def tearDown(self) -> None:
        pass
    def test_invest_success(self):
        pass