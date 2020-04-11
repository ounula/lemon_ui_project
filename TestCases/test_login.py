# -*- coding: UTF-8 –*-
#author: zhh
#time: 2020/4/12 0:32
import  unittest
from selenium import webdriver
from PageObjects.login_p import LoginPage
class TestLogin(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get('http://120.78.128.25:8765/Index/login.html')

    def tearDown(self) -> None:
        self.driver.quit()
    #正常用例 - 登陆成功
    def test_login_success(self):
        lg=loginPage(self.driver)

    #异常用例 - 手机号码不正确
    def test_login_user_errorUser(self):
        pass

    #异常用例 - 用户名为空
    def test_login_noUser(self):
        pass
