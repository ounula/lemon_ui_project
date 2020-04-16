# -*- encoding:utf-8 -*-
# @Time : 2020/4/16 17:22 
# @Author : ZHH
from PageLocators.ptsdList_locator import PtsdList as loc
from Common.basepage import BasePage

class PtsdList(BasePage):
    def list_exist(self):
        doc = "刷新普通送达列表"
        self.wait_elementsPresent(loc.ptsd_data,doc=doc)


    def new_ptsd(self):
        doc = "点击新建普通送达"
        self.click_element(loc.create_ptsd,doc=doc)

