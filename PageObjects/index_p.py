# -*- coding: UTF-8 –*-
#author: zhh
#time: 2020/4/11 23:59
from selenium import webdriver
from PageLocators.homepage_locator import HomePageLocator as loc
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from Common.logger import Log
from Common.basepage import BasePage
class IndexPage(BasePage):
    # def __init__(self,driver):
    #     self.driver=driver
    #     self.driver=webdriver.Chrome()

    def isExist_logout_ele(self):
        doc="主页登出按钮"
        self.wait_eleVisible(loc.logOut,doc=doc)
        return self.get_element(loc.logOut,doc=doc)

    #选标操作
    def select_first_bid(self):
        pass
    #随机选标
    def select_random_bid(self):
        eles=self.driver.find_elements()