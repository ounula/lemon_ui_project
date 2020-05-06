# -*- encoding:utf-8 -*-
# @Time : 2020/4/13 12:44 
# @Author : ZHH
from selenium import webdriver
from Common import dir_config
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time, datetime
from selenium.webdriver.common.by import By
from Common.logger import Log
import os
from Common import dir_config

username = 'zhh'
password = '123456'


def login(func):
    def fun():
        user = input("请输入账号：")
        pw = input("请输入密码：")
        if username == user and pw == password:
            func()
        else:
            print("账号或密码错误")

    return fun


# @login  # @login：语法糖   --> index = login(index)
def index():
    print("登陆成功")


# index()
index = login(index)
print(index())