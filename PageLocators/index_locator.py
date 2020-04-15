# -*- coding: UTF-8 –*-
#author: zhh
#time: 2020/4/13 7:18
from selenium.webdriver.common.by import By

class IndexLocator:
    #注销
    logOut = (By.XPATH,'//span[text()="注销"]')
    #普通送达菜单
    ptsd = (By.XPATH,'//li[contains(text(),"普通")]')
    #新建普通送达
    create_ptsd = (By.XPATH,'//span[contains(text(),"新建普通送达")]')