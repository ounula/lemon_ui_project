# -*- coding: UTF-8 –*-
#author: zhh
#time: 2020/4/12 0:00
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from PageLocators.loginpage_locator import LoginPageLocator as loc
from Common.basepage import BasePage

class LoginPage(BasePage):
    #登录
    def login(self,username,password,remember_user=True):
        #输入用户名、密码，点击登录
        doc = "登录页面_登录功能"
        self.wait_eleVisible(loc.name_text)
        self.input_text(loc.name_text,username,doc)
        self.input_text(loc.pwd_text,password,doc)
        self.click_element(loc.login_but,doc)
        # 判断是否勾选保存用户名
        if not remember_user:
            self.click_element(loc.remember_me,doc)

    #获取用户名下方错误提示信息
    def pleaseInputUser(self):
        doc = "登录页面_登录区域错误提示"
        self.wait_eleVisible(loc.errMSG_loginArea,doc=doc)
        return self.get_text(loc.errMSG_loginArea,doc=doc)

    #获取页面正中错误提示信息
    def noRegist_wrongPasswd(self):
        doc = "登录页面_中间区域错误提示"
        self.wait_eleVisible(loc.errMSG_midArea,doc=doc)
        return self.get_text(loc.errMSG_midArea,doc=doc)