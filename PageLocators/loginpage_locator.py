# -*- coding: UTF-8 –*-
#author: zhh
#time: 2020/4/12 14:19
from selenium.webdriver.common.by import By
class LoginPageLocator:
    name_text = (By.XPATH,'//input[@placeholder="请输入您的用户名"]')
    pwd_text = (By.XPATH,'//input[@placeholder="请输入您的密码"]')
    login_but = (By.XPATH,'//button[@class="el-button el-button--primary"]')
    #错误提示框-密码不足6位
    errMSG_6passwd =  (By.XPATH,'//div[contains(text(),"至少6位数的密码")]')
    #错误提示框-请输入账号
    errMSG_no_input_user = (By.XPATH,'//div[contains(text(),"请输入账号")]')
    #人机验证
    rebot_forbid =(By.ID,'//div[@id="nc_1__scale_text"]')