# -*- encoding:utf-8 -*-
# @Time : 2020/4/13 12:44 
# @Author : ZHH
from selenium import webdriver
from Common.filepath import FilePath
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time,datetime
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
a=driver.find_element_by_xpath('123')
a.get_attribute()