# -*- coding: UTF-8 –*-
#author: zhh
#time: 2020/4/14 7:33
import pytest
from selenium import webdriver
from PageObjects.login_p import LoginPage
from PageObjects.index_p import IndexPage
from Common.basepage import BasePage
from TestDatas import common_datas as CD
from TestDatas import login_datas as LD
from PageLocators.loginpage_locator import LoginPageLocator

#pytest.mark
def pytest_configure(config):
    marker_list = ["login"]  # 在此定义mark标签列表
    for markers in marker_list:
        config.addinivalue_line("markers", markers)

driver = None
#声明fixture，测试类前/后置操作
@pytest.fixture(scope="class")
def access_web():
    global driver
    #前置操作
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(CD.web_login_url)
    lg=LoginPage(driver)
    yield (driver,lg)#分割线；返回值
    #后置操作
    driver.quit()

#声明fixture，用例前/后置操作
@pytest.fixture()
def refresh_page():
    #前置操作
    yield
    #后置操作
    driver.refresh()

@pytest.fixture()
def clear_login_text():
    yield
    doc ="清除元素文本"
    BasePage().clear_text(LoginPageLocator.name_text,doc=doc)
    BasePage().clear_text(LoginPageLocator.pwd_text,doc=doc)

#声明fixture，会话前/后置操作
@pytest.fixture(scope="session")
def session_demo():
    print("测试会话前置")
    yield
    print("测试会话后置")