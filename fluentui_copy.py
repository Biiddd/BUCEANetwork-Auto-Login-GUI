# Form implementation generated from reading ui file 'form_fluent_copy.ui'
#
# Created by: PyQt6 UI code generator 6.5.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Widget(object):
    def setupUi(self, Widget):
        Widget.setObjectName("Widget")
        Widget.resize(640, 340)
        self.gridLayout = QtWidgets.QGridLayout(Widget)
        self.gridLayout.setContentsMargins(3, 3, 3, 3)
        self.gridLayout.setHorizontalSpacing(3)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.btn = QtWidgets.QGridLayout()
        self.btn.setContentsMargins(2, 30, 15, 5)
        self.btn.setObjectName("btn")
        self.save_config_btn = PrimaryPushButton(parent=Widget)
        self.save_config_btn.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.save_config_btn.setFont(font)
        self.save_config_btn.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.save_config_btn.setCheckable(False)
        self.save_config_btn.setChecked(False)
        self.save_config_btn.setObjectName("save_config_btn")
        self.btn.addWidget(self.save_config_btn, 3, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.btn.addItem(spacerItem, 0, 0, 1, 1)
        self.login_btn = PrimaryPushButton(parent=Widget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.login_btn.setFont(font)
        self.login_btn.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.login_btn.setObjectName("login_btn")
        self.btn.addWidget(self.login_btn, 1, 0, 1, 1)
        self.startwithwin = TransparentTogglePushButton(parent=Widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.startwithwin.sizePolicy().hasHeightForWidth())
        self.startwithwin.setSizePolicy(sizePolicy)
        self.startwithwin.setMinimumSize(QtCore.QSize(106, 40))
        self.startwithwin.setMaximumSize(QtCore.QSize(118, 40))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.startwithwin.setFont(font)
        self.startwithwin.setObjectName("startwithwin")
        self.btn.addWidget(self.startwithwin, 5, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.btn.addItem(spacerItem1, 4, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.btn.addItem(spacerItem2, 2, 0, 1, 1)
        self.gridLayout.addLayout(self.btn, 1, 1, 2, 1)
        self.email = QtWidgets.QGridLayout()
        self.email.setContentsMargins(15, 2, 7, 11)
        self.email.setVerticalSpacing(3)
        self.email.setObjectName("email")
        self.Hidestmp = PushButton(parent=Widget)
        self.Hidestmp.setText("")
        self.Hidestmp.setObjectName("Hidestmp")
        self.email.addWidget(self.Hidestmp, 3, 1, 1, 1)
        self.email_account_input = LineEdit(parent=Widget)
        self.email_account_input.setMinimumSize(QtCore.QSize(260, 33))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(12)
        self.email_account_input.setFont(font)
        self.email_account_input.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.email_account_input.setObjectName("email_account_input")
        self.email.addWidget(self.email_account_input, 1, 0, 1, 1)
        self.email_account_label = QtWidgets.QLabel(parent=Widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.email_account_label.sizePolicy().hasHeightForWidth())
        self.email_account_label.setSizePolicy(sizePolicy)
        self.email_account_label.setMaximumSize(QtCore.QSize(62, 16777215))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(14)
        self.email_account_label.setFont(font)
        self.email_account_label.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.email_account_label.setStyleSheet("backgroud-color: #009faa;\n"
"color: white;\n"
"border-radius: 5px;\n"
"padding: 1px")
        self.email_account_label.setObjectName("email_account_label")
        self.email.addWidget(self.email_account_label, 0, 0, 1, 1)
        self.stmp_passwd_input = LineEdit(parent=Widget)
        self.stmp_passwd_input.setMinimumSize(QtCore.QSize(260, 33))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(12)
        self.stmp_passwd_input.setFont(font)
        self.stmp_passwd_input.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.stmp_passwd_input.setObjectName("stmp_passwd_input")
        self.email.addWidget(self.stmp_passwd_input, 3, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.email.addItem(spacerItem3, 2, 2, 1, 1)
        self.stmp_passwd_label = QtWidgets.QLabel(parent=Widget)
        self.stmp_passwd_label.setMaximumSize(QtCore.QSize(118, 16777215))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(14)
        self.stmp_passwd_label.setFont(font)
        self.stmp_passwd_label.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.stmp_passwd_label.setStyleSheet("backgroud-color:#009faa;\n"
"color:white;\n"
"border-radius: 5px;\n"
"padding: 1px")
        self.stmp_passwd_label.setObjectName("stmp_passwd_label")
        self.email.addWidget(self.stmp_passwd_label, 2, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.email.addItem(spacerItem4, 2, 1, 1, 1)
        self.Hideemail = PushButton(parent=Widget)
        self.Hideemail.setText("")
        self.Hideemail.setObjectName("Hideemail")
        self.email.addWidget(self.Hideemail, 1, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.email.addItem(spacerItem5, 2, 3, 1, 1)
        self.gridLayout.addLayout(self.email, 3, 0, 1, 1)
        self.account_info = QtWidgets.QGridLayout()
        self.account_info.setContentsMargins(10, -1, 7, 3)
        self.account_info.setSpacing(3)
        self.account_info.setObjectName("account_info")
        self.rest_pocket_label = QtWidgets.QLabel(parent=Widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rest_pocket_label.sizePolicy().hasHeightForWidth())
        self.rest_pocket_label.setSizePolicy(sizePolicy)
        self.rest_pocket_label.setMinimumSize(QtCore.QSize(120, 0))
        self.rest_pocket_label.setMaximumSize(QtCore.QSize(120, 40))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(14)
        self.rest_pocket_label.setFont(font)
        self.rest_pocket_label.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.rest_pocket_label.setStyleSheet("background-color: #009faa;\n"
"color: white;\n"
"border-radius: 5px;\n"
"padding: 1px")
        self.rest_pocket_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.rest_pocket_label.setObjectName("rest_pocket_label")
        self.account_info.addWidget(self.rest_pocket_label, 0, 0, 1, 1)
        self.used_flow_label = QtWidgets.QLabel(parent=Widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.used_flow_label.sizePolicy().hasHeightForWidth())
        self.used_flow_label.setSizePolicy(sizePolicy)
        self.used_flow_label.setMinimumSize(QtCore.QSize(98, 0))
        self.used_flow_label.setMaximumSize(QtCore.QSize(121, 40))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(14)
        self.used_flow_label.setFont(font)
        self.used_flow_label.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.used_flow_label.setStyleSheet("background-color: #009faa;\n"
"color: white;\n"
"border-radius: 5px;\n"
"padding: 1px")
        self.used_flow_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.used_flow_label.setObjectName("used_flow_label")
        self.account_info.addWidget(self.used_flow_label, 0, 1, 1, 1)
        self.count_label = QtWidgets.QLabel(parent=Widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.count_label.sizePolicy().hasHeightForWidth())
        self.count_label.setSizePolicy(sizePolicy)
        self.count_label.setMinimumSize(QtCore.QSize(98, 0))
        self.count_label.setMaximumSize(QtCore.QSize(97, 40))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(14)
        self.count_label.setFont(font)
        self.count_label.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.count_label.setStyleSheet("background-color: #009faa;\n"
"color: white;\n"
"border-radius: 5px;\n"
"padding: 1px")
        self.count_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.count_label.setObjectName("count_label")
        self.account_info.addWidget(self.count_label, 0, 2, 1, 1)
        self.rest_pocket = QtWidgets.QLabel(parent=Widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rest_pocket.sizePolicy().hasHeightForWidth())
        self.rest_pocket.setSizePolicy(sizePolicy)
        self.rest_pocket.setMinimumSize(QtCore.QSize(130, 0))
        self.rest_pocket.setMaximumSize(QtCore.QSize(160, 40))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(12)
        self.rest_pocket.setFont(font)
        self.rest_pocket.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.rest_pocket.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.rest_pocket.setObjectName("rest_pocket")
        self.account_info.addWidget(self.rest_pocket, 1, 0, 1, 1)
        self.used_flow = QtWidgets.QLabel(parent=Widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.used_flow.sizePolicy().hasHeightForWidth())
        self.used_flow.setSizePolicy(sizePolicy)
        self.used_flow.setMinimumSize(QtCore.QSize(130, 0))
        self.used_flow.setMaximumSize(QtCore.QSize(120, 40))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(12)
        self.used_flow.setFont(font)
        self.used_flow.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.used_flow.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.used_flow.setObjectName("used_flow")
        self.account_info.addWidget(self.used_flow, 1, 1, 1, 1)
        self.count = QtWidgets.QLabel(parent=Widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.count.sizePolicy().hasHeightForWidth())
        self.count.setSizePolicy(sizePolicy)
        self.count.setMinimumSize(QtCore.QSize(130, 0))
        self.count.setMaximumSize(QtCore.QSize(120, 40))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(12)
        self.count.setFont(font)
        self.count.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.count.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.count.setObjectName("count")
        self.account_info.addWidget(self.count, 1, 2, 1, 1)
        self.gridLayout.addLayout(self.account_info, 2, 0, 1, 1)
        self.input = QtWidgets.QGridLayout()
        self.input.setContentsMargins(15, -1, -1, 0)
        self.input.setHorizontalSpacing(7)
        self.input.setVerticalSpacing(3)
        self.input.setObjectName("input")
        self.passwd_label = QtWidgets.QLabel(parent=Widget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(14)
        self.passwd_label.setFont(font)
        self.passwd_label.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.passwd_label.setStyleSheet("background-color: #009faa;\n"
"color: white;\n"
"border-radius: 5px;\n"
"padding: 1px")
        self.passwd_label.setObjectName("passwd_label")
        self.input.addWidget(self.passwd_label, 0, 4, 1, 2)
        self.Hidepasswd = PushButton(parent=Widget)
        self.Hidepasswd.setMaximumSize(QtCore.QSize(32, 16777215))
        self.Hidepasswd.setText("")
        self.Hidepasswd.setObjectName("Hidepasswd")
        self.input.addWidget(self.Hidepasswd, 2, 5, 1, 1)
        self.ip = QtWidgets.QLabel(parent=Widget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(14)
        self.ip.setFont(font)
        self.ip.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.ip.setObjectName("ip")
        self.input.addWidget(self.ip, 4, 4, 1, 1)
        self.passwd_input = LineEdit(parent=Widget)
        self.passwd_input.setMinimumSize(QtCore.QSize(205, 33))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(12)
        self.passwd_input.setFont(font)
        self.passwd_input.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.passwd_input.setObjectName("passwd_input")
        self.input.addWidget(self.passwd_input, 2, 4, 1, 1)
        self.account_label = QtWidgets.QLabel(parent=Widget)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(14)
        self.account_label.setFont(font)
        self.account_label.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.account_label.setStyleSheet("background-color: #009faa;\n"
"color: white;\n"
"border-radius: 5px;\n"
"padding: 1px")
        self.account_label.setObjectName("account_label")
        self.input.addWidget(self.account_label, 0, 0, 1, 2)
        self.IP_label = QtWidgets.QLabel(parent=Widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.IP_label.sizePolicy().hasHeightForWidth())
        self.IP_label.setSizePolicy(sizePolicy)
        self.IP_label.setMaximumSize(QtCore.QSize(76, 16777215))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(14)
        self.IP_label.setFont(font)
        self.IP_label.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.IP_label.setStyleSheet("background-color: #009faa;\n"
"color: white;\n"
"border-radius: 5px;\n"
"padding: 1px")
        self.IP_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.IP_label.setObjectName("IP_label")
        self.input.addWidget(self.IP_label, 4, 0, 1, 2)
        self.account_input = LineEdit(parent=Widget)
        self.account_input.setMinimumSize(QtCore.QSize(205, 33))
        self.account_input.setMaximumSize(QtCore.QSize(250, 33))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(12)
        self.account_input.setFont(font)
        self.account_input.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.account_input.setObjectName("account_input")
        self.input.addWidget(self.account_input, 2, 0, 1, 2)
        self.gridLayout.addLayout(self.input, 1, 0, 1, 1)

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        _translate = QtCore.QCoreApplication.translate
        Widget.setWindowTitle(_translate("Widget", "Widget"))
        self.save_config_btn.setText(_translate("Widget", "保存设置"))
        self.login_btn.setText(_translate("Widget", "登录"))
        self.startwithwin.setText(_translate("Widget", "开机自启"))
        self.email_account_label.setText(_translate("Widget", " 邮箱"))
        self.stmp_passwd_label.setText(_translate("Widget", " STMP秘钥"))
        self.rest_pocket_label.setText(_translate("Widget", "校园网余额"))
        self.used_flow_label.setText(_translate("Widget", "已使用流量"))
        self.count_label.setText(_translate("Widget", "计费区间"))
        self.rest_pocket.setText(_translate("Widget", "不在校园网中"))
        self.used_flow.setText(_translate("Widget", "不在校园网中"))
        self.count.setText(_translate("Widget", "不在校园网中"))
        self.passwd_label.setText(_translate("Widget", "密码（默认身份证后六位）"))
        self.ip.setText(_translate("Widget", "Unknown"))
        self.account_label.setText(_translate("Widget", "校园网账号（学号）"))
        self.IP_label.setText(_translate("Widget", " 当前IP"))
from qfluentwidgets import LineEdit, PrimaryPushButton, PushButton, TransparentTogglePushButton
