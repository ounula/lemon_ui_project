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
import collections
from Common.win_controller import WinControl
from selenium import webdriver
from Common.win_controller import WinControl,MicroSIP

# driver = webdriver.Chrome()
# driver.get("https://www.layui.com/demo/upload.html")
# driver.implicitly_wait(10)
# driver.find_element_by_id('test2').click()
# WinControl().upload_file('C:\\','wallpaper.png')
MicroSIP(dir_config.MicroSip_dir)