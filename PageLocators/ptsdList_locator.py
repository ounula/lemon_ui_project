# -*- encoding:utf-8 -*-
# @Time : 2020/4/16 16:35 
# @Author : ZHH
from selenium.webdriver.common.by import By
class PtsdList:
    #新建普通送达
    create_ptsd = ("新建普通送达按钮",(By.XPATH,'//span[contains(text(),"新建普通送达")]'))
    #暂无数据div
    no_data_now = ("普通送达列表-暂无数据",(By.XPATH,'//div[@class="el-table__empty-block"]'))
    #列表数据
    ptsd_data = ("普通送达列表",(By.XPATH,'//tr[@class="el-table__row"]'))
    #下载回证
    down_re = ("下载回证按钮",(By.XPATH,'//span[text()="查询"]'))
    #受送达人标题
    ssdr_titile = ("受送达人标题",(By.XPATH,'//h3[text()="受送达人信息"]'))