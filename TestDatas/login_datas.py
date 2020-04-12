# -*- coding: UTF-8 –*-
#author: zhh
#time: 2020/4/12 8:25

#正常场景
success_data = {"user":"18684720553","passwd":"python"}

#异常用例   -   号码格式错(大于11位，小于11位，为空，不存在的号码段)
phone_data = [
    {"user":"186847205538","passwd":"python","result":"请输入正确的手机号"},
    {"user":"18684720","passwd":"python","result":"请输入正确的手机号"},
    {"user":"","passwd":"python","result":"请输入手机号"},
    {"user": "11184742666", "passwd": "python", "result": "请输入正确的手机号"}
]

#异常用例 - 号码未注册或密码错误
wrong_passwd_data = [
    {"user":"17712857416","passwd":"python","result":"此账号没有经过授权，请联系管理员!"},
    {"user":"18684720553","passwd":"python321","result":"帐号或密码错误!"}
]