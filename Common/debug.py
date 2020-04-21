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
import collections

words = ["yo", "ew", "fc", "zrc", "yodn", "fcm", "qm", "qmo", "fcmz", "z", "ewq", "yod", "ewqz", "y"]


def dsadas():
    a = []
    b = sorted(list(i for i in words if len(i) == max(len(k) for k in words)))
    for i in range(len(b)):
        for j in range(len(b[i])):
            if a in words:
                a.append(b[i][j])
            # else:
            #     break
        return b[i]

a = os.listdir(dir_config.downloads_dir)
print(type(a))
# tu = (i for i in range(10))
# print(next(tu))
# print(next(tu))