# -*- coding: UTF-8 –*-
#author: zhh
#time: 2020/4/11 23:59
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
class IndexPage:
    def __init__(self,driver):
        self.driver=driver

    def isExist_logout_ele(self):
        #如果登出按钮存在
        try:
            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,'//a[@href="/Index/logout.html"]')))
            return True
        except:
            return False