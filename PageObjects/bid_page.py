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
        pass

    #投资