# -*- coding: UTF-8 –*-
# @author: zhh
# @time: 2020/5/2 16:31
from pywinauto.application import Application
from Common.logger import Log

# 打开指定软件
class WinControl:
    def open_software(self, softwarePath, doc=""):
        try:
            app = Application(backend="uia").start(softwarePath)
            Log().log_info(doc+"开启成功")
        except:
            Log().log_error(doc+"开启失败")