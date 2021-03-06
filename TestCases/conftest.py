# -*- coding: UTF-8 –*-
# author: zhh
# time: 2020/4/14 7:33
import pytest
from selenium import webdriver
from Common import dir_config
from PageObjects.index_p import IndexPage
from PageObjects.login_p import LoginPage
import os
from TestDatas import common_datas as CD
from TestDatas import login_datas as LD


# pytest.mark
def pytest_configure(config):
    marker_list = ["login"]  # 在此定义mark标签列表
    for markers in marker_list:
        config.addinivalue_line("markers", markers)


driver = None


# driver=webdriver.Chrome()
# 声明fixture，测试类前/后置操作
# 类：前置开启登录页面，后置关闭浏览器
@pytest.fixture(scope="class")
def access_web():
    global driver
    # 前置操作
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(CD.web_login_url)
    lg = LoginPage(driver)
    yield driver, lg  # 分割线；返回值
    # 后置操作
    driver.quit()


# 用例：后置刷新
@pytest.fixture()
def refresh_page():
    yield
    driver.refresh()


# 用例：后置后退
@pytest.fixture()
def back_page():
    yield
    driver.back()


@pytest.fixture(scope="class")
def login_success():
    global driver
    # 前置操作
    options = webdriver.ChromeOptions()
    prefs = {
        "download.prompt_for_download": False,
        'download.default_directory': dir_config.downloads_dir,  # 下载目录
        "plugins.always_open_pdf_externally": True,
        'profile.default_content_settings.popups': 0,  # 设置为0，禁止弹出窗口
    }
    options.add_experimental_option('prefs', prefs)
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get(CD.web_login_url)
    LoginPage(driver).login(LD.success_data["用户名"], LD.success_data["密码"])
    yield driver


@pytest.fixture(scope="class")
def get_ptsd_page():
    global driver
    # 前置操作
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(CD.web_login_url)
    LoginPage(driver).login(LD.success_data["用户名"], LD.success_data["密码"])
    IndexPage(driver).click_ptsd()
    yield driver
    driver.quit()


# 声明fixture，会话前/后置操作
@pytest.fixture(scope="session")
def session_demo():
    print("测试会话前置")
    yield
    print("测试会话后置")
