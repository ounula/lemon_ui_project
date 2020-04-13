# -*- coding: UTF-8 –*-
#author: zhh
#time: 2020/4/13 7:17
from selenium.webdriver.common.by import By
class BidPageLocator:
    #融合投标（表示进入该页面）
    ronghetoubiao=(By.XPATH,'//div[@class="float_left sub_tit_sty"]')
    #可用余额
    canUseMoney=(By.XPATH,'//input[@class="form-control invest-unit-investinput"]')


