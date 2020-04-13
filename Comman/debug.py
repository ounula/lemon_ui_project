# -*- encoding:utf-8 -*-
# @Time : 2020/4/13 12:44 
# @Author : ZHH
import datetime,time
a=time.time()
time.sleep(2.11)
# b=datetime.datetime.now()
b=time.time()
c='%.1f' %(b-a)
print(c)