# -*- coding: UTF-8 –*-
#author: zhh
#time: 2020/4/12 14:19
from selenium.webdriver.common.by import By
class LoginPageLocator:
    name_text = (By.XPATH,'//input[@name="phone"]')
    pwd_text = (By.XPATH,'//input[@name="password"]')
    login_but = (By.XPATH,'//button[text()="登录"]')
    #错误提示框-登陆区域
    errMSG_loginArea =  (By.XPATH,'//div[@class="form-error-info"]')
    #错误提示框-中间区域
    errMSG_midArea = (By.XPATH,'//div[@class="layui-layer-content"]')
    #记住我
    remember_me = (By.XPATH,'//input[@name="remember_me"]')