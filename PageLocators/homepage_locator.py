# -*- coding: UTF-8 –*-
#author: zhh
#time: 2020/4/13 7:18
from selenium.webdriver.common.by import By

class HomePageLocator:
    # 抢投标
    qiangTB=(By.XPATH,'//a[@class="btn btn-special"]')
    #注销
    logOut=(By.XPATH,'//span[text()="注销"]')