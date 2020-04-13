# -*- coding: UTF-8 –*-
#author: zhh
#time: 2020/4/11 23:59
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from PageLocators.homepage_locator import HomePageLocator as loc
import random
class IndexPage:
    def __init__(self,driver):
        # self.driver=driver
        self.driver=webdriver.Chrome()

    def isExist_logout_ele(self):
        #如果登出按钮存在
        try:
            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((loc.logOut)))
            return True
        except:
            return False

    #选标操作
    def select_first_bid(self):
        pass
    #随机选标
    def select_random_bid(self):
        try:
            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((loc.qiangtb)))
            eles=self.driver.find_elements(loc.qiangtb)
            eles=eles[random.randint(0,len(eles)-1)]
            return eles
        except:
            return  None