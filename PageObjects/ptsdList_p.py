# -*- encoding:utf-8 -*-
# @Time : 2020/4/16 17:22 
# @Author : ZHH
from PageLocators.ptsdList_locator import PtsdList as loc
from Common.basepage import BasePage


class PtsdList(BasePage):
    def list_exist(self):
        doc = "普通送达列表"
        self.wait_elementsPresent(loc.ptsd_data, doc=doc)
        return self.get_elements(loc.ptsd_data, doc=doc)

    def new_ptsd(self):
        doc = "点击新建普通送达"
        self.wait_eleVisible(loc.create_ptsd, doc=doc)
        self.click_element(loc.create_ptsd, doc=doc)

    def download_receipt_noWoker(self):
        doc = "不勾选工单，点击下载回证"
        self.click_element(loc.down_re, doc=doc)

    def reset_query(self):
        doc = "点击重置按钮"
        self.click_element(loc.reset_button, doc=doc)
