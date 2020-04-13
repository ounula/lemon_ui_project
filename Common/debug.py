# -*- encoding:utf-8 -*-
# @Time : 2020/4/13 12:44 
# @Author : ZHH
from selenium import webdriver
from Common import dir_config
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time,datetime
from selenium.webdriver.common.by import By
a=time.strftime("%Y-%m-%d-%H-%M-%S"), time.localtime()
b=time.localtime()
print(a)
print(b)
