# -*- encoding:utf-8 -*-
# @Time : 2020/4/13 12:15 
# @Author : ZHH
import logging
from Common import dir_config
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time,datetime
from selenium import webdriver
#封装基本函数 - 执行日志、异常处理、失败截图
#所有页面公共的部分
class BasePage:
    def __init__(self,driver):
        self.driver = driver

    #等待元素可见
    def wait_eleVisible(self,locator,wait_times=20,poll_frequency=0.5,doc=""):
        # ''''
        # :param locator: 元素定位，元祖形式
        # :param times: 最长等待时间
        # :param poll_frequency: 轮询间隔
        # :param doc: 模块名_页面名称_操作名称
        # :return:
        # '''
        logging.info("等待元素{0}可见".format(locator))
        try:
            #开始等待时间
            start = time.time()
            WebDriverWait(self.driver, wait_times,poll_frequency).until(EC.visibility_of_element_located((locator)))
            #结束等待的时间点
            end = time.time()
            #求差值
            wait_time = '%.1f' %(end-start)
            logging.info("找到元素，花费{0}秒".format(wait_time))
        except:
            logging.exception("定位元素超时")
            #截图
            self.save_screenshot(doc)
            raise

    #等待元素存在
    def wait_elePresent(self,locator,wait_times=20,poll_frequency=0.5,doc=""):
        '''

        :param locator: 元素定位，元祖形式
        :param times: 最长等待时间
        :param poll_frequency: 轮询间隔
        :param doc: 模块名_页面名称_操作名称
        :return:
        '''
        logging.info("判断网页存在元素{0}".format(locator))
        try:
            # 开始等待时间
            start = time.time()
            WebDriverWait(self.driver,wait_times, poll_frequency).until(EC.presence_of_element_located((locator)))
            # 结束等待的时间点
            end = time.time()
            # 求差值
            wait_time = '%.1f' % (end - start)
            logging.info("网页存在元素，花费{0}秒".format(wait_time))
        except:
            logging.exception("定位元素超时")
            # 截图
            self.save_screenshot(doc)
            raise

    #查找元素
    def get_element(self,locator,doc=""):
        logging.info("开始查找元素:{}".format(locator))
        try:
            ele = self.driver.find_element(*locator)
            return ele
        except:
            logging.exception("查找元素失败！")
            #截图
            self.save_screenshot(doc)
            raise

    #点击操作
    def click_element(self,locator,doc=""):
        ele = self.get_element(locator,doc=doc)
        logging.info("{0}   点击元素：{1}".format(doc,locator))
        try:
            ele.click()
        except:
            logging.exception("元素点击操作失败！")
            #  截图
            self.save_screenshot(doc)
            raise

    #输入操作
    def input_text(self,locator,text,doc=""):
        ele = self.get_element(locator,doc=doc)
        try:
            ele.send_keys(text)
        except:
            logging.exception("输入操作失败！")
            #  截图
            self.save_screenshot(doc)
            raise

    #获取元素的文本内容
    def get_text(self,locator,doc=""):
        ele = self.get_element(locator, doc=doc)
        try:
            return ele.text
        except:
            logging.exception("获取元素文本失败！")
            #  截图
            self.save_screenshot(doc)
            raise

    #获取元素属性
    def get_element_attribute(self,locator,attr,doc=""):
        ele = self.get_element(locator, doc=doc)
        try:
            return ele.get_attribute(attr)
        except:
            logging.exception("输入操作失败！")
            #  截图
            self.save_screenshot(doc)
            raise

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


    #截图
    def save_screenshot(self,doc):
        #图片名称：模块名_页面名称_操作名称_年-月-日_时分秒.png
        filePath = dir_config.screenshot_dir+\
            "/{0}_{1}.png".format(doc,time.strftime("%Y-%m-%d-%H-%M-%S"))
        try:
            self.driver.save_screenshot(filePath)
            logging.info("截屏成功，图片路径为{}".format(filePath))
        except:
            logging.exception("截图失败")

