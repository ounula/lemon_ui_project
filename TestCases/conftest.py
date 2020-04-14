# -*- coding: UTF-8 –*-
#author: zhh
#time: 2020/4/14 7:33
import pytest
from selenium import webdriver
from PageObjects.login_p import LoginPage
from PageObjects.index_p import IndexPage
from TestDatas import common_datas as CD
from TestDatas import login_datas as LD

driver = None
#声明fixture
@pytest.fixture(scope="class")
def access_web():
    global driver
    #前置操作
    driver = webdriver.Chrome()
    driver.get(CD.web_login_url)
    lg=LoginPage(driver)
    yield (driver,lg)#分割线；返回值
    driver.quit()
    #后置操作

@pytest.fixture()
def refresh_page():
    #前置操作
    yield
    #后置操作
    driver.refresh()