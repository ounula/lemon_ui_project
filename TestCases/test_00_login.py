# -*- coding: UTF-8 –*-
#author: zhh
#time: 2020/4/12 0:32
from selenium import webdriver
from PageObjects.login_p import LoginPage
from PageObjects.index_p import IndexPage
from TestDatas import common_datas as CD
from TestDatas import login_datas as LD
from Common.logger import Log
import pytest

@pytest.mark.usefixtures("access_web")
@pytest.mark.usefixtures("refresh_page")
class TestLogin:
    Log().log_info('====================开始测试登录模块=====================')
    # def test_error_error(self):
    #     assert 3==5
    #  异常用例 - 登录信息不正确 (大于11位，小于11位，空)    ddt
    @pytest.mark.parametrize("data",LD.phone_data)
    def test_login_user_errorUser(self,data,access_web):
        Log().log_info("**********异常用例：登录账号不正确**********")
        access_web[1].login(data["user"],data["passwd"])
        assert access_web[1].pleaseInputUser(),data["result"]

    @pytest.mark.parametrize("data",LD.wrong_passwd_data)
    def test_login_noExistUser_wrongPasswd(self,data,access_web):
        Log().log_info("**********异常用例：登录密码不正确、无权限**********")
        access_web[1].login(data["user"],data["passwd"])
        assert access_web[1].noRegist_wrongPasswd(),data['result']


    #正常用例 - 登陆成功
    @pytest.mark.login
    def test_login_success(self,access_web):#fixture函数作为参数，接收fixture返回值\
        Log().log_info("**********登录用例：正常场景：使用正确的用户名和密码登录**********")
        access_web[1].login(LD.success_data["user"],LD.success_data["passwd"])
        assert IndexPage(access_web[0]).isExist_logout_ele()
