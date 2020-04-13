# -*- coding: UTF-8 –*-
#author: zhh
#time: 2020/4/12 20:07
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
class BidPage:
    def __init__(self,driver):
        self.driver=webdriver.Chrome()
        # self.driver=driver

    #投资
    def invest(self):
        pass

    #获取用户余额
    def get_user_money(self):
        WebDriverWait(self.driver,20).until(EC.visibility_of_element_located)
        pass

    #投资成功提示框 -点击查看并激活
    def click_activeButton_on_success_popup(self):
        pass

    #错误提示框 - 非100的整数倍、请正确填写投标金额
    def please_input_corectMoney(self):
        pass