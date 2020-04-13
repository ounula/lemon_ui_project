# -*- coding: UTF-8 –*-
#author: zhh
#time: 2020/4/12 0:32
import  unittest
from selenium import webdriver
from PageObjects.login_p import LoginPage
from PageObjects.index_p import IndexPage
from TestDatas import common_datas as CD
from TestDatas import login_datas as LD
import ddt

@ddt.ddt
class TestLogin(unittest.TestCase):
    #测试类前置条件
    @classmethod
    def setUpClass(cls):
        print("==========开始测试登陆模块==========")
        cls.driver = webdriver.Chrome()
        cls.driver.get(CD.web_login_url)
        cls.lg=LoginPage(cls.driver)
    #测试用例前置条件
    def setUp(self):
        pass
        #设置无头浏览器
        # option=webdriver.ChromeOptions()
        # option.headless = True
        # self.driver = webdriver.Chrome(options=option)
        # self.driver = webdriver.Chrome()
        # self.driver.get(CD.web_login_url)
        # self. lg=LoginPage(self.driver)
    #测试用例后置
    def tearDown(self):
        self.driver.refresh()

    #测试类后置
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


    #正常用例 - 登陆成功
    def test_login_2_success(self):
        self.lg.login(LD.success_data["user"],LD.success_data["passwd"])
        self.assertTrue(IndexPage(self.driver).isExist_logout_ele())

    #异常用例 - 手机号码不正确 (大于11位，小于11位，空)    ddt
    @ddt.data(*LD.phone_data)
    def test_login_1_user_errorUser(self,data):
        self.lg.login(data["user"],data["passwd"])
        self.assertEqual(self.lg.pleaseInputUser(),data["result"])

    @ddt.data(*LD.wrong_passwd_data)
    def test_login_0_noExistUser_wrongPasswd(self,data):
        self.lg.login(data["user"],data["passwd"])
        self.assertEqual(self.lg.noRegist_wrongPasswd(),data['result'])

