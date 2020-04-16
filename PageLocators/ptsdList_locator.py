# -*- encoding:utf-8 -*-
# @Time : 2020/4/16 16:35 
# @Author : ZHH
from selenium.webdriver.common.by import By
class PtsdList:
    #新建普通送达
    create_ptsd = (By.XPATH,'//span[contains(text(),"新建普通送达")]')