import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QCheckBox, QPushButton
from qframelesswindow import FramelessWindow, StandardTitleBar
from PyQt6.QtCore import QFile
from login import login
from fluentui import Ui_Widget
import json
import os
import shutil
from pathlib import Path


class MyWindow(FramelessWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui = Ui_Widget()  # 创建UI对象
        self.ui.setupUi(self)  # 在窗口上设置UI

        # 连接登录按钮的点击事件到处理函数
        self.ui.login_btn.clicked.connect(self.login_and_send_email)
        # 连接保存设置按钮的点击事件到处理函数
        self.ui.save_config_btn.clicked.connect(self.save_config)
        # 设置两个密码框为密码模式
        self.ui.passwd_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.ui.stmp_passwd_input.setEchoMode(QLineEdit.EchoMode.Password)
        # 初始化密码框显示状态变量
        self.password_visible = False
        self.stmp_password_visible = False
        # 连接显示密码 checkbox 的点击事件到处理函数
        self.ui.hidepasswd.clicked.connect(self.toggle_password_display)
        self.ui.stmp_hidepasswd.clicked.connect(self.toggle_stmp_password_display)
        self.ui.startwithwin.stateChanged.connect(self.toggle_startup)
        # 读取并填充JSON文件中的信息
        self.load_saved_settings()
        app.setStyleSheet(open('style.qss').read())
    def load_saved_settings(self):
        try:
            with open('setting.json', 'r') as json_file:
                account_info = json.load(json_file)
                username = account_info.get('username', '')
                password = account_info.get('password', '')
                email = account_info.get('email', '')
                email_password = account_info.get('email_password', '')

                self.ui.account_input.setText(username)
                self.ui.passwd_input.setText(password)
                self.ui.email_account_input.setText(email)
                self.ui.stmp_passwd_input.setText(email_password)
        except FileNotFoundError:
            pass

    def toggle_startup(self, state):
        if state == QCheckBox.clicked:
            self.create_startup_shortcut()
        else:
            self.remove_startup_shortcut()

    def create_startup_shortcut(self):
        # 获取当前脚本所在的目录
        current_directory = Path(__file__).parent
        shortcut_path = os.path.join(current_directory, "auto_login.lnk")
        print("已创建快捷方式")

        # 将快捷方式复制到启动文件夹
        startup_folder = Path(os.path.expanduser(
            "~")) / "AppData" / "Roaming" / "Microsoft" / "Windows" / "Start Menu" / "Programs" / "Startup"
        shutil.copy2(shortcut_path, startup_folder)
        print("已添加自启动")

    def remove_startup_shortcut(self):
        # 获取启动文件夹位置
        startup_folder = Path(os.path.expanduser(
            "~")) / "AppData" / "Roaming" / "Microsoft" / "Windows" / "Start Menu" / "Programs" / "Startup"

        # 删除快捷方式
        shortcut_path = os.path.join(startup_folder, "auto_login.lnk")
        if os.path.exists(shortcut_path):
            os.remove(shortcut_path)
            print("已删除自启动")

    def toggle_password_display(self):
        # 切换密码框的显示模式
        self.password_visible = not self.password_visible
        self.ui.passwd_input.setEchoMode(
            QLineEdit.EchoMode.Normal if self.password_visible else QLineEdit.EchoMode.Password)

    def toggle_stmp_password_display(self):
        # 切换密码框的显示模式
        self.stmp_password_visible = not self.stmp_password_visible
        self.ui.stmp_passwd_input.setEchoMode(
            QLineEdit.EchoMode.Normal if self. stmp_password_visible else QLineEdit.EchoMode.Password)

    def login_and_send_email(self,):
        # 从UI获取用户名、密码、邮箱等信息
        username = self.ui.account_input.text()
        password = self.ui.passwd_input.text()
        email_account = self.ui.email_account_input.text()
        email_password = self.ui.stmp_passwd_input.text()

        # 调用 login 函数并传递 email 和 email_password
        ip_address, used_flow, rest_pocket = login(username, password, email_account, email_password)
        # 设置 IP 标签的文本
        self.ui.ip.setText(ip_address)

        self.ui.used_flow.setText(str(used_flow))
        # 将其转化为浮点数，并使用 round 函数将小数位数限制为两位
        rest_pocket_float = float(rest_pocket)
        rest_pocket_rounded = round(rest_pocket_float, 2)
        # 将其转回字符串并添加 "元"
        rest_pocket_formatted = f"{rest_pocket_rounded}元"
        self.ui.rest_pocket.setText(rest_pocket_formatted)
        # if isinstance(used_flow, float):
        #     print(f"{used_flow} 是一个浮点数。")
        # else:
        #     print(f"{used_flow} 不是一个浮点数。")

        if 0 <= float(used_flow[:-3]) < 20:
            self.ui.count.setText("免费区间")
        elif 20 < float(used_flow[:-3]) <= 300:
            self.ui.count.setText("0.5元/GB")
        else:
            self.ui.count.setText("1元/GB")

    def save_config(self):
        # 从UI获取用户名、密码、邮箱等信息
        username = self.ui.account_input.text()
        password = self.ui.passwd_input.text()
        email = self.ui.email_account_input.text()
        email_password = self.ui.stmp_passwd_input.text()

        # 保存页面设置为JSON文件
        account_info = {
            'username': username,
            'password': password,
            'email': email,
            'email_password': email_password
        }
        with open('setting.json', 'w') as json_file:
            json.dump(account_info, json_file)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
