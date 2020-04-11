# -*- coding: UTF-8 –*-
#author: zhh
#time: 2020/4/12 0:32
import  unittest
from selenium import webdriver
from PageObjects.login_p import LoginPage
from PageObjects.index_p import IndexPage
class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://120.78.128.25:8765/Index/login.html')
        self. lg=LoginPage(self.driver)

    def tearDown(self):
        self.driver.quit()
    #正常用例 - 登陆成功
    def test_login_success(self):
        self.lg.login('18684720553','python')
        self.assertTrue(IndexPage(self.driver).isExist_logout_ele())
    #异常用例 - 手机号码不正确     ddt
    def test_login_user_errorUser(self):
        self.lg.login('1868472', 'python')
        self.assertFalse(IndexPage(self.driver).isExist_logout_ele())

    #异常用例 - 用户名为空
    def test_login_noUser(self):
        self.lg.login('', 'python')
        self.assertFalse(IndexPage(self.driver).isExist_logout_ele())
