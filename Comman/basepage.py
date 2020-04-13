# -*- encoding:utf-8 -*-
# @Time : 2020/4/13 12:15 
# @Author : ZHH
import logging
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
#封装基本函数 - 执行日志、异常处理、失败截图
#所有页面公共的部分
class BasePage:
    def __init__(self,driver):
        self.driver = driver

    #等待元素可见
    def wait_eleVisible(self,locator,times=20,poll_frequency=0.5):
        logging.info("等待元素{0}可见".format(locator))
        try:
            #开始等待时间
            start = time.time()
            WebDriverWait(self.driver, times,poll_frequency).until(EC.visibility_of_element_located((locator)))
            #结束等待的时间点
            end = time.time()
            #求差值
            wait_time = '%.1f' %(end-start)
            logging.info("找到元素，花费{0}秒".format(wait_time))
        except:
            logging.exception("定位元素超时")


    #等待元素存在
    def wait_elePresent(self):
        pass

    #查找元素
    def get_element(self):
        pass

    #点击操作
    def click_element(self):
        pass

    #输入操作
    def input_text(self):
        pass

    #获取元素的文本内容
    def get_text(self):
        pass

    #获取元素属性
    def get_element_attribute(self):
        pass

    #alert处理
    def alert_action(self,action="accept"):
        pass

    #iframe切换
    def switch_iframe(self,ifirame_refernce):
        pass

    #上传操作
    def upload_file(self):
        pass

    #滚动条处理
    #窗口切换
