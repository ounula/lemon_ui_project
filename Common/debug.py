# -*- encoding:utf-8 -*-
# @Time : 2020/4/13 12:44 
# @Author : ZHH
from selenium import webdriver
from Common import dir_config
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time, datetime
from selenium.webdriver.common.by import By
from Common.logger import Log
import os
from Common import dir_config

a = os.listdir(dir_config.downloads_dir)
print(type(a))
# tu = (i for i in range(10))
# print(next(tu))
# print(next(tu))