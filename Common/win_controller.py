# -*- coding: UTF-8 –*-
# @author: zhh
# @time: 2020/5/2 16:31
from pywinauto.application import Application
from Common.logger import Log
from Common.dir_config import MicroSip_dir
from time import sleep

class WinControl:
    # 打开指定软件
    def open_software(self, softwarePath, doc=""):
        try:
            #启动软件
            app = Application('uia').start(MicroSip_dir)
            sleep(2)
            app2 = Application('uia').connect(path=MicroSip_dir)
            dlg = app2['MicroSIP']
            Log().log_info(doc+"开启成功")
        except:
            Log().log_error(doc+"开启失败")


app = Application('uia').start(MicroSip_dir)
sleep(2)
app2 = Application('uia').connect(path=MicroSip_dir)
dlg = app2['MicroSIP']
combox_1 = dlg['ComboBox']
edit = combox_1.child_window(auto_id="1001", control_type="Edit")
#截图需安装pillow
pic = dlg.capture_as_image()
# pic.save('01.png')
Log().log_info("开启成功")