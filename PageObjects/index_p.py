# -*- coding: UTF-8 –*-
#author: zhh
#time: 2020/4/11 23:59
from selenium import webdriver
from PageLocators.index_locator import IndexLocator as loc
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
        doc="主页注销按钮"
        self.wait_eleVisible(loc.logOut,doc=doc)
        return self.get_element(loc.logOut,doc=doc)

    def select_first_bid(self):
        doc="菜单选择普通送达"
        self.wait_eleVisible(loc.ptsd)
        pass
    #随机选标
    def select_random_bid(self):
        eles=self.driver.find_elements()