# -*- coding: UTF-8 –*-
#author: zhh
#time: 2020/4/12 0:00
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
class LoginPage:
    def __init__(self,driver):
        self.driver = webdriver.Chrome()

    #登录
    def login(self,username,password,remember_user=True):
        #输入用户名、密码，点击登录
        WebDriverWait(self.driver,20).until(EC.visibility_of_element_located((By.XPATH,'//input[@name="phone"]')))
        name_text = '//input[@name="phone"]'
        pwd_text = '//input[@name="password"]'
        login_but = '//button[text()="登录"'
        self.driver.find_element_by_xpath(name_text).send_keys(username)
        self.driver.find_element_by_xpath(pwd_text).send_keys(password)
        self.driver.find_element_by_xpath(login_but).click()
        # 判断是否勾选保存用户名
        if not remember_user:
            self.driver.find_element_by_xpath('//input[@name="remember_me"]').click()


    #注册
    #找回密码