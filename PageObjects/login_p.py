# -*- coding: UTF-8 –*-
#author: zhh
#time: 2020/4/12 0:00
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from PageLocators.loginpage_locator import LoginPageLocator as loc
class LoginPage:
    def __init__(self,driver):
        # self.driver = webdriver.Chrome()
        self.driver = driver
    #登录
    def login(self,username,password,remember_user=True):
        #输入用户名、密码，点击登录
        WebDriverWait(self.driver,20).until(EC.visibility_of_element_located((loc.name_text)))
        self.driver.find_element(*loc.name_text).send_keys(username)
        self.driver.find_element(*loc.pwd_text).send_keys(password)
        self.driver.find_element(*loc.login_but).click()
        # 判断是否勾选保存用户名
        if not remember_user:
            self.driver.find_element(*loc.remember_me).click()

    #获取用户名下方错误提示信息
    def pleaseInputUser(self):
        try:
            WebDriverWait(self.driver,20).until(EC.visibility_of_element_located((loc.errMSG_loginArea)))
            return self.driver.find_element(*loc.errMSG_loginArea).text
        except:
            return None

    #获取页面正中错误提示信息
    def noRegist_wrongPasswd(self):
        try:
            WebDriverWait(self.driver,20).until(EC.visibility_of_element_located((loc.errMSG_midArea)))
            return self.driver.find_element(*loc.errMSG_midArea).text
        except:
            return None