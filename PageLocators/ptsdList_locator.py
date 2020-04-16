# -*- encoding:utf-8 -*-
# @Time : 2020/4/16 16:35 
# @Author : ZHH
from selenium.webdriver.common.by import By
class PtsdList:
    #新建普通送达
    create_ptsd = (By.XPATH,'//span[contains(text(),"新建普通送达")]')
    #暂无数据div
    no_data_now = (By.XPATH,'//div[@class="el-table__empty-block"]')
    #列表数据
    ptsd_data = (By.XPATH,'//tr[@class="el-table__row"]')