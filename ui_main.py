# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QButtonGroup, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QPushButton, QRadioButton, QSizePolicy,
    QSpacerItem, QSpinBox, QStackedWidget, QTableView,
    QVBoxLayout, QWidget)

class Ui_Home(object):
    def setupUi(self, Home):
        if not Home.objectName():
            Home.setObjectName(u"Home")
        Home.resize(642, 737)
        self.homeWidget = QWidget(Home)
        self.homeWidget.setObjectName(u"homeWidget")
        self.homeWidget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.homeWidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.mainStackWidget = QStackedWidget(self.homeWidget)
        self.mainStackWidget.setObjectName(u"mainStackWidget")
        self.login_page = QWidget()
        self.login_page.setObjectName(u"login_page")
        self.login_page.setStyleSheet(u"#login_page {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, \n"
"                stop:0 #6a11cb, stop:1 #2575fc);\n"
"}\n"
"#login_card_frame {\n"
"    background-color: rgba(255, 255, 255, 0.95); \n"
"    border-radius: 20px;\n"
"    border: 1px solid rgba(255, 255, 255, 0.3);\n"
"}\n"
"\n"
"QLineEdit {\n"
"    background-color: #f8f9fa;\n"
"    border: 2px solid #e9ecef;\n"
"    border-radius: 12px;\n"
"    padding: 12px;\n"
"    font-size: 14px;\n"
"    color: #495057;\n"
"    margin-bottom: 5px;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 2px solid #3498db;\n"
"    background-color: #ffffff;\n"
"}\n"
"\n"
"QLabel#username_label_login, QLabel#password_label_login {\n"
"    color: #576574; \n"
"    font-size: 11px;\n"
"    font-weight: bold;\n"
"    text-transform: uppercase;\n"
"    margin-bottom: 2px;\n"
"}\n"
"\n"
"#welcome_label_login {\n"
"    color: #2c3e50; \n"
"    font-family: \"Segoe UI Semibold\", \"Trebuchet MS\";\n"
"    font-size: 28px;\n"
"    font-weight: 700;\n"
"    lette"
                        "r-spacing: 0.5px;\n"
"    padding-bottom: 15px; \n"
"    border-bottom: 2px solid #3498db; \n"
"}\n"
"\n"
"#subtitle_label_login {\n"
"    color: #95a5a6;\n"
"    font-size: 13px;\n"
"    margin-bottom: 20px;\n"
"}\n"
"\n"
"QPushButton#login_btn_login {\n"
"    background-color: #3498db;\n"
"    color: white;\n"
"    font-weight: bold;\n"
"    font-size: 15px;\n"
"    border-radius: 12px;\n"
"    padding: 12px;\n"
"    min-width: 120px;\n"
"}\n"
"\n"
"QPushButton#login_btn_login:hover {\n"
"    background-color: #2980b9;\n"
"}\n"
"\n"
"QPushButton#login_btn_login:pressed {\n"
"    background-color: #1d6fa5; \n"
"    padding-top: 12px; \n"
"    padding-left: 14px;\n"
"}\n"
"\n"
"QPushButton#signup_btn_login {\n"
"    background-color: transparent;\n"
"    color: #3498db;\n"
"    font-weight: bold;\n"
"    border: 2px solid #3498db;\n"
"    border-radius: 12px;\n"
"    padding: 10px;\n"
"    min-width: 120px;\n"
"}\n"
"\n"
"QPushButton#signup_btn_login:hover {\n"
"    background-color: #f0f7ff;\n"
"} \n"
"\n"
"Q"
                        "PushButton#signup_btn_login:pressed {\n"
"    background-color: #d6eaf8; \n"
"    border: 2px solid #2980b9;\n"
"}")
        self.gridLayout = QGridLayout(self.login_page)
        self.gridLayout.setObjectName(u"gridLayout")
        self.login_card_frame = QFrame(self.login_page)
        self.login_card_frame.setObjectName(u"login_card_frame")
        self.login_card_frame.setMinimumSize(QSize(400, 0))
        self.login_card_frame.setMaximumSize(QSize(450, 16777215))
        self.login_card_frame.setStyleSheet(u"")
        self.login_card_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.login_card_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_8 = QGridLayout(self.login_card_frame)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.signup_btn_login = QPushButton(self.login_card_frame)
        self.signup_btn_login.setObjectName(u"signup_btn_login")

        self.gridLayout_8.addWidget(self.signup_btn_login, 6, 1, 1, 1)

        self.username_login_frame = QFrame(self.login_card_frame)
        self.username_login_frame.setObjectName(u"username_login_frame")
        self.username_login_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.username_login_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.username_login_frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.username_label_login = QLabel(self.username_login_frame)
        self.username_label_login.setObjectName(u"username_label_login")
        font = QFont()
        font.setBold(True)
        self.username_label_login.setFont(font)

        self.horizontalLayout_2.addWidget(self.username_label_login)

        self.username_lineedit_login = QLineEdit(self.username_login_frame)
        self.username_lineedit_login.setObjectName(u"username_lineedit_login")

        self.horizontalLayout_2.addWidget(self.username_lineedit_login)


        self.gridLayout_8.addWidget(self.username_login_frame, 2, 0, 2, 4)

        self.login_btn_login = QPushButton(self.login_card_frame)
        self.login_btn_login.setObjectName(u"login_btn_login")

        self.gridLayout_8.addWidget(self.login_btn_login, 6, 2, 1, 1)

        self.login_horizontalspacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_8.addItem(self.login_horizontalspacer, 6, 3, 1, 1)

        self.password_login_frame = QFrame(self.login_card_frame)
        self.password_login_frame.setObjectName(u"password_login_frame")
        self.password_login_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.password_login_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.password_login_frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.password_label_login = QLabel(self.password_login_frame)
        self.password_label_login.setObjectName(u"password_label_login")
        self.password_label_login.setFont(font)

        self.horizontalLayout_3.addWidget(self.password_label_login)

        self.password_lineedit_login = QLineEdit(self.password_login_frame)
        self.password_lineedit_login.setObjectName(u"password_lineedit_login")

        self.horizontalLayout_3.addWidget(self.password_lineedit_login)


        self.gridLayout_8.addWidget(self.password_login_frame, 5, 0, 1, 4)

        self.signup_horizontalspacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_8.addItem(self.signup_horizontalspacer, 6, 0, 1, 1)

        self.welcome_label_login = QLabel(self.login_card_frame)
        self.welcome_label_login.setObjectName(u"welcome_label_login")
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setWeight(QFont.ExtraBold)
        self.welcome_label_login.setFont(font1)
        self.welcome_label_login.setStyleSheet(u"#welcome_label_login {\n"
"    color: #2c3e50;\n"
"    font-size: 28px;\n"
"    font-weight: 800;\n"
"    font-family: 'Segoe UI', sans-serif;\n"
"}")

        self.gridLayout_8.addWidget(self.welcome_label_login, 0, 1, 1, 2, Qt.AlignmentFlag.AlignHCenter)

        self.subtitle_label_login = QLabel(self.login_card_frame)
        self.subtitle_label_login.setObjectName(u"subtitle_label_login")

        self.gridLayout_8.addWidget(self.subtitle_label_login, 1, 0, 1, 4, Qt.AlignmentFlag.AlignHCenter)


        self.gridLayout.addWidget(self.login_card_frame, 1, 1, 1, 1)

        self.loginframe_left_horizontalspacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.loginframe_left_horizontalspacer, 1, 0, 1, 1)

        self.loginframe_right_horizontalspacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.loginframe_right_horizontalspacer, 1, 2, 1, 1)

        self.loginframe_above_verticalspacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.loginframe_above_verticalspacer, 0, 0, 1, 3)

        self.loginframe_below_verticalspacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.loginframe_below_verticalspacer, 2, 0, 1, 3)

        self.mainStackWidget.addWidget(self.login_page)
        self.home_page = QWidget()
        self.home_page.setObjectName(u"home_page")
        self.horizontalLayout = QHBoxLayout(self.home_page)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.sidebar_frame_home = QFrame(self.home_page)
        self.sidebar_frame_home.setObjectName(u"sidebar_frame_home")
        self.sidebar_frame_home.setMinimumSize(QSize(170, 0))
        self.sidebar_frame_home.setMaximumSize(QSize(300, 16777215))
        self.sidebar_frame_home.setStyleSheet(u"#sidebar_frame_home {\n"
"    background-color: #2c3e50;\n"
"    border: none;\n"
"}\n"
"\n"
"#menu_sidebar_label_home {\n"
"    color: #ffffff;\n"
"    font-size: 18px;\n"
"    font-weight: bold;\n"
"    font-family: \"Segoe UI\", sans-serif;\n"
"    padding: 20px 10px 10px 20px;\n"
"    letter-spacing: 1px;\n"
"    text-transform: uppercase;\n"
"}\n"
"\n"
"#sidebar_frame_home QPushButton {\n"
"    color: #bdc3c7; \n"
"    background-color: transparent;\n"
"    border: none;\n"
"    border-radius: 0px;\n"
"    text-align: left;\n"
"    padding: 15px 25px;\n"
"    font-size: 14px;\n"
"    font-weight: 500;\n"
"    font-family: \"Segoe UI\", sans-serif;\n"
"}\n"
"\n"
"#sidebar_frame_home QPushButton:hover {\n"
"    color: #ffffff;\n"
"    background-color: #34495e; \n"
"    border-left: 4px solid #3498db; \n"
"}\n"
"\n"
"QPushButton#logout_sidebar_btn_home:hover {\n"
"    background-color: #e74c3c; \n"
"    color: white;\n"
"}\n"
"\n"
"#sidebar_frame_home QPushButton:pressed {\n"
"    background-color: #1abc9c;"
                        "\n"
"    color: white;\n"
"}")
        self.sidebar_frame_home.setFrameShape(QFrame.Shape.StyledPanel)
        self.sidebar_frame_home.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.sidebar_frame_home)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.menu_sidebar_label_home = QLabel(self.sidebar_frame_home)
        self.menu_sidebar_label_home.setObjectName(u"menu_sidebar_label_home")
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setBold(True)
        self.menu_sidebar_label_home.setFont(font2)

        self.verticalLayout_2.addWidget(self.menu_sidebar_label_home)

        self.createquiz_sidebar_btn_home = QPushButton(self.sidebar_frame_home)
        self.createquiz_sidebar_btn_home.setObjectName(u"createquiz_sidebar_btn_home")
        self.createquiz_sidebar_btn_home.setStyleSheet(u"")
        self.createquiz_sidebar_btn_home.setAutoDefault(False)
        self.createquiz_sidebar_btn_home.setFlat(False)

        self.verticalLayout_2.addWidget(self.createquiz_sidebar_btn_home)

        self.attendquiz_sidebar_btn_home = QPushButton(self.sidebar_frame_home)
        self.attendquiz_sidebar_btn_home.setObjectName(u"attendquiz_sidebar_btn_home")
        self.attendquiz_sidebar_btn_home.setStyleSheet(u"")

        self.verticalLayout_2.addWidget(self.attendquiz_sidebar_btn_home)

        self.results_sidebar_btn_home = QPushButton(self.sidebar_frame_home)
        self.results_sidebar_btn_home.setObjectName(u"results_sidebar_btn_home")
        self.results_sidebar_btn_home.setStyleSheet(u"")

        self.verticalLayout_2.addWidget(self.results_sidebar_btn_home)

        self.logout_sidebar_btn_home = QPushButton(self.sidebar_frame_home)
        self.logout_sidebar_btn_home.setObjectName(u"logout_sidebar_btn_home")
        self.logout_sidebar_btn_home.setStyleSheet(u"")

        self.verticalLayout_2.addWidget(self.logout_sidebar_btn_home)

        self.sidebar_verticalspacer = QSpacerItem(20, 369, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.sidebar_verticalspacer)


        self.horizontalLayout.addWidget(self.sidebar_frame_home)

        self.homepage_stackwidget = QStackedWidget(self.home_page)
        self.homepage_stackwidget.setObjectName(u"homepage_stackwidget")
        self.attendquiz_stackwidget_page = QWidget()
        self.attendquiz_stackwidget_page.setObjectName(u"attendquiz_stackwidget_page")
        self.verticalLayout_3 = QVBoxLayout(self.attendquiz_stackwidget_page)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.select_qs_number_frame = QFrame(self.attendquiz_stackwidget_page)
        self.select_qs_number_frame.setObjectName(u"select_qs_number_frame")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.select_qs_number_frame.sizePolicy().hasHeightForWidth())
        self.select_qs_number_frame.setSizePolicy(sizePolicy)
        self.select_qs_number_frame.setStyleSheet(u"QFrame#select_qs_number_frame {\n"
"    background-color: #ffffff;\n"
"    border-radius: 15px;\n"
"    border: 1px solid #e0e6ed;\n"
"}\n"
"\n"
"QLabel#select_qs_number_label {\n"
"    color: #34495e;\n"
"    font-size: 18px;\n"
"    font-weight: bold;\n"
"    font-family: \"Segoe UI\", sans-serif;\n"
"}\n"
"\n"
"QSpinBox#select_qs_number_spinbox {\n"
"    background-color: #f8f9fa;\n"
"    border: 2px solid #dcdde1;\n"
"    border-radius: 8px;\n"
"    padding: 2px;\n"
"    min-width: 60px;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QSpinBox#select_qs_number_spinbox:focus {\n"
"    border: 2px solid #2ecc71; \n"
"}\n"
"\n"
"QPushButton#start_quiz_btn {\n"
"    background-color: #2ecc71; \n"
"    color: white;\n"
"    font-weight: bold;\n"
"    font-size: 15px;\n"
"    border-radius: 10px;\n"
"    padding: 10px 20px;\n"
"    text-transform: uppercase;\n"
"}\n"
"\n"
"QPushButton#start_quiz_btn:hover {\n"
"    background-color: #27ae60;\n"
"}\n"
"\n"
"QPushButton#start_quiz_btn:pressed {\n"
"    background-color: #"
                        "1e8449;\n"
"    padding-top: 12px; \n"
"}")
        self.select_qs_number_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.select_qs_number_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_5 = QGridLayout(self.select_qs_number_frame)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.select_qs_number_horizontalspacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_5.addItem(self.select_qs_number_horizontalspacer, 0, 2, 1, 1)

        self.select_qs_number_spinbox = QSpinBox(self.select_qs_number_frame)
        self.select_qs_number_spinbox.setObjectName(u"select_qs_number_spinbox")
        self.select_qs_number_spinbox.setMaximumSize(QSize(50, 16777215))
        font3 = QFont()
        self.select_qs_number_spinbox.setFont(font3)

        self.gridLayout_5.addWidget(self.select_qs_number_spinbox, 0, 1, 1, 1)

        self.start_quiz_btn = QPushButton(self.select_qs_number_frame)
        self.start_quiz_btn.setObjectName(u"start_quiz_btn")
        self.start_quiz_btn.setFont(font)
        self.start_quiz_btn.setStyleSheet(u"")

        self.gridLayout_5.addWidget(self.start_quiz_btn, 1, 0, 1, 1, Qt.AlignmentFlag.AlignLeft)

        self.select_qs_number_label = QLabel(self.select_qs_number_frame)
        self.select_qs_number_label.setObjectName(u"select_qs_number_label")
        self.select_qs_number_label.setMaximumSize(QSize(250, 16777215))
        self.select_qs_number_label.setFont(font2)

        self.gridLayout_5.addWidget(self.select_qs_number_label, 0, 0, 1, 1, Qt.AlignmentFlag.AlignTop)


        self.verticalLayout_3.addWidget(self.select_qs_number_frame)

        self.quiz_qs_frame = QFrame(self.attendquiz_stackwidget_page)
        self.quiz_qs_frame.setObjectName(u"quiz_qs_frame")
        sizePolicy.setHeightForWidth(self.quiz_qs_frame.sizePolicy().hasHeightForWidth())
        self.quiz_qs_frame.setSizePolicy(sizePolicy)
        self.quiz_qs_frame.setStyleSheet(u"#quiz_qs_frame {\n"
"    background-color: #ffffff;\n"
"    border-radius: 20px;\n"
"    border: 1px solid #e0e6ed;\n"
"    padding: 20px;\n"
"}\n"
"\n"
"#quiz_qs_label {\n"
"    color: #2c3e50;\n"
"    font-size: 18px;\n"
"    font-weight: bold;\n"
"    margin-bottom: 20px;\n"
"}\n"
"\n"
"QRadioButton {\n"
"    color: #4b5563;\n"
"    font-size: 14px;\n"
"    padding: 12px;\n"
"    background-color: #f9fafb;\n"
"    border: 2px solid #f3f4f6;\n"
"    border-radius: 10px;\n"
"    spacing: 10px;\n"
"}\n"
"\n"
"QRadioButton:hover {\n"
"    background-color: #f0f7ff;\n"
"    border: 2px solid #3498db;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width: 18px;\n"
"    height: 18px;\n"
"}\n"
"\n"
"QRadioButton:checked {\n"
"    background-color: #ebf5fb;\n"
"    border: 2px solid #3498db;\n"
"    color: #2980b9;\n"
"    font-weight: bold;\n"
"}")
        self.quiz_qs_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.quiz_qs_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_4 = QGridLayout(self.quiz_qs_frame)
        self.gridLayout_4.setSpacing(15)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.quiz_qs_label = QLabel(self.quiz_qs_frame)
        self.quiz_qs_label.setObjectName(u"quiz_qs_label")
        self.quiz_qs_label.setFont(font)

        self.gridLayout_4.addWidget(self.quiz_qs_label, 0, 0, 1, 1, Qt.AlignmentFlag.AlignLeft)

        self.qs_opt0_radio = QRadioButton(self.quiz_qs_frame)
        self.quiz_qs_frame_btngrp = QButtonGroup(Home)
        self.quiz_qs_frame_btngrp.setObjectName(u"quiz_qs_frame_btngrp")
        self.quiz_qs_frame_btngrp.addButton(self.qs_opt0_radio)
        self.qs_opt0_radio.setObjectName(u"qs_opt0_radio")
        self.qs_opt0_radio.setFont(font3)

        self.gridLayout_4.addWidget(self.qs_opt0_radio, 1, 0, 1, 1)

        self.qs_opt1_radio = QRadioButton(self.quiz_qs_frame)
        self.quiz_qs_frame_btngrp.addButton(self.qs_opt1_radio)
        self.qs_opt1_radio.setObjectName(u"qs_opt1_radio")
        self.qs_opt1_radio.setFont(font3)

        self.gridLayout_4.addWidget(self.qs_opt1_radio, 2, 0, 1, 1)

        self.qs_opt2_radio = QRadioButton(self.quiz_qs_frame)
        self.quiz_qs_frame_btngrp.addButton(self.qs_opt2_radio)
        self.qs_opt2_radio.setObjectName(u"qs_opt2_radio")
        self.qs_opt2_radio.setFont(font3)

        self.gridLayout_4.addWidget(self.qs_opt2_radio, 3, 0, 1, 1)

        self.qs_opt3_radio = QRadioButton(self.quiz_qs_frame)
        self.quiz_qs_frame_btngrp.addButton(self.qs_opt3_radio)
        self.qs_opt3_radio.setObjectName(u"qs_opt3_radio")
        self.qs_opt3_radio.setFont(font3)

        self.gridLayout_4.addWidget(self.qs_opt3_radio, 4, 0, 1, 1)

        self.next_qs_btn = QPushButton(self.quiz_qs_frame)
        self.next_qs_btn.setObjectName(u"next_qs_btn")
        self.next_qs_btn.setFont(font)
        self.next_qs_btn.setStyleSheet(u"QPushButton#next_qs_btn {\n"
"    background-color: #3498db;\n"
"    color: white;\n"
"    font-weight: bold;\n"
"    font-size: 14px;\n"
"    border-radius: 10px;\n"
"    padding: 10px 30px;\n"
"    min-width: 100px;\n"
"}\n"
"\n"
"QPushButton#next_qs_btn:hover {\n"
"    background-color: #2980b9;\n"
"}\n"
"\n"
"QPushButton#next_qs_btn:pressed {\n"
"    background-color: #1c5980;\n"
"    padding-top: 12px;\n"
"}")

        self.gridLayout_4.addWidget(self.next_qs_btn, 5, 0, 1, 1, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout_3.addWidget(self.quiz_qs_frame)

        self.show_result_frame = QFrame(self.attendquiz_stackwidget_page)
        self.show_result_frame.setObjectName(u"show_result_frame")
        sizePolicy.setHeightForWidth(self.show_result_frame.sizePolicy().hasHeightForWidth())
        self.show_result_frame.setSizePolicy(sizePolicy)
        self.show_result_frame.setStyleSheet(u"#show_result_frame {\n"
"    background-color: #ffffff;\n"
"    border-radius: 20px;\n"
"    border: 2px solid #2ecc71; \n"
"    padding: 30px;\n"
"}\n"
"\n"
"#show_result_label {\n"
"    color: #2c3e50;\n"
"    font-size: 26px;\n"
"    font-weight: 900;\n"
"    font-family: \"Segoe UI\", sans-serif;\n"
"    margin-bottom: 20px;\n"
"}\n"
"\n"
"#restart_quiz_btn {\n"
"    background-color: #f39c12;\n"
"    color: white;\n"
"    font-weight: bold;\n"
"    font-size: 14px;\n"
"    border-radius: 10px;\n"
"    padding: 12px 25px;\n"
"    text-transform: uppercase;\n"
"}\n"
"\n"
"#restart_quiz_btn:hover {\n"
"    background-color: #e67e22;\n"
"}\n"
"\n"
"#restart_quiz_btn:pressed {\n"
"    background-color: #d35400;\n"
"    padding-top: 14px;\n"
"}")
        self.show_result_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.show_result_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_6 = QGridLayout(self.show_result_frame)
        self.gridLayout_6.setSpacing(20)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.restart_quiz_btn = QPushButton(self.show_result_frame)
        self.restart_quiz_btn.setObjectName(u"restart_quiz_btn")
        self.restart_quiz_btn.setMaximumSize(QSize(170, 16777215))
        self.restart_quiz_btn.setFont(font)

        self.gridLayout_6.addWidget(self.restart_quiz_btn, 3, 0, 1, 1, Qt.AlignmentFlag.AlignLeft)

        self.show_result_label = QLabel(self.show_result_frame)
        self.show_result_label.setObjectName(u"show_result_label")
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        font4.setWeight(QFont.Black)
        self.show_result_label.setFont(font4)
        self.show_result_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_6.addWidget(self.show_result_label, 2, 0, 1, 1)

        self.show_result_frame_horizontalspacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_6.addItem(self.show_result_frame_horizontalspacer, 2, 1, 1, 1)


        self.verticalLayout_3.addWidget(self.show_result_frame)

        self.attendquiz_verticalspacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.attendquiz_verticalspacer)

        self.homepage_stackwidget.addWidget(self.attendquiz_stackwidget_page)
        self.createquiz_stackwidget_page = QWidget()
        self.createquiz_stackwidget_page.setObjectName(u"createquiz_stackwidget_page")
        self.createquiz_stackwidget_page.setStyleSheet(u"#createquiz_stackwidget_page {\n"
"    background-color: transparent; \n"
"}\n"
"\n"
"#add_new_qs_frame{\n"
"	background-color: white;\n"
"    border-radius: 20px;\n"
"    padding: 0px;\n"
"    border: 1px solid #e0e6ed;\n"
"}\n"
"\n"
"#all_qs_frame {\n"
"    background-color: white;\n"
"    border-radius: 20px;\n"
"    padding: 2px;\n"
"    border: 1px solid #e0e6ed;\n"
"}\n"
"\n"
"QLabel {\n"
"    font-size: 11px;\n"
"    font-weight: bold;\n"
"    text-transform: uppercase;\n"
"    color: #64748b;\n"
"    margin-bottom: 2px;\n"
"}\n"
"\n"
"#add_new_qs_label {\n"
"    color: #1a2a6c;\n"
"    font-size: 24px;\n"
"    font-weight: bold;\n"
"    margin-bottom: 0px;\n"
"}\n"
"\n"
"#all_qs_label{\n"
"    color: #1a2a6c;\n"
"    font-size: 16px;\n"
"    font-weight: bold;\n"
"    margin-bottom: 10px;\n"
"\n"
"}\n"
"\n"
"QLineEdit {\n"
"    background-color: #f8f9fa;\n"
"    border: 2px solid #e9ecef;\n"
"    border-radius: 10px;\n"
"    padding: 5px;\n"
"    font-size: 13px;\n"
"    color: #2c3e50;\n"
"}\n"
"\n"
""
                        "QLineEdit:focus {\n"
"    border: 2px solid #3498db;\n"
"    background-color: white;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: #3498db;\n"
"    color: white;\n"
"    font-weight: bold;\n"
"    border-radius: 10px;\n"
"    padding: 7px;\n"
"    min-width: 120px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #2980b9;\n"
"}\n"
"\n"
"#show_all_qs_btn {\n"
"    background-color: transparent;\n"
"    color: #3498db;\n"
"    border: 2px solid #3498db;\n"
"}\n"
"\n"
"#show_all_qs_btn:hover {\n"
"    background-color: #f0f7ff;\n"
"}")
        self.gridLayout_3 = QGridLayout(self.createquiz_stackwidget_page)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.add_new_qs_frame = QFrame(self.createquiz_stackwidget_page)
        self.add_new_qs_frame.setObjectName(u"add_new_qs_frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.add_new_qs_frame.sizePolicy().hasHeightForWidth())
        self.add_new_qs_frame.setSizePolicy(sizePolicy1)
        self.add_new_qs_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.add_new_qs_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.add_new_qs_frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.add_new_qs_label = QLabel(self.add_new_qs_frame)
        self.add_new_qs_label.setObjectName(u"add_new_qs_label")
        self.add_new_qs_label.setFont(font)
        self.add_new_qs_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.add_new_qs_label, 0, Qt.AlignmentFlag.AlignLeft)

        self.question_frame = QFrame(self.add_new_qs_frame)
        self.question_frame.setObjectName(u"question_frame")
        self.question_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.question_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.question_frame)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.createquiz_qs_label = QLabel(self.question_frame)
        self.createquiz_qs_label.setObjectName(u"createquiz_qs_label")
        self.createquiz_qs_label.setFont(font)

        self.horizontalLayout_5.addWidget(self.createquiz_qs_label)

        self.createquiz_qs_lineedit = QLineEdit(self.question_frame)
        self.createquiz_qs_lineedit.setObjectName(u"createquiz_qs_lineedit")

        self.horizontalLayout_5.addWidget(self.createquiz_qs_lineedit)


        self.verticalLayout_4.addWidget(self.question_frame)

        self.answer_frame = QFrame(self.add_new_qs_frame)
        self.answer_frame.setObjectName(u"answer_frame")
        self.answer_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.answer_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.answer_frame)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.createquiz_ans_label = QLabel(self.answer_frame)
        self.createquiz_ans_label.setObjectName(u"createquiz_ans_label")
        self.createquiz_ans_label.setFont(font)

        self.horizontalLayout_8.addWidget(self.createquiz_ans_label)

        self.createquiz_ans_lineedit = QLineEdit(self.answer_frame)
        self.createquiz_ans_lineedit.setObjectName(u"createquiz_ans_lineedit")

        self.horizontalLayout_8.addWidget(self.createquiz_ans_lineedit)


        self.verticalLayout_4.addWidget(self.answer_frame)

        self.createquiz_other_option_label = QLabel(self.add_new_qs_frame)
        self.createquiz_other_option_label.setObjectName(u"createquiz_other_option_label")
        self.createquiz_other_option_label.setFont(font)

        self.verticalLayout_4.addWidget(self.createquiz_other_option_label)

        self.opt1_frame = QFrame(self.add_new_qs_frame)
        self.opt1_frame.setObjectName(u"opt1_frame")
        self.opt1_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.opt1_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.opt1_frame)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.createquiz_opt1_label = QLabel(self.opt1_frame)
        self.createquiz_opt1_label.setObjectName(u"createquiz_opt1_label")
        self.createquiz_opt1_label.setFont(font)

        self.horizontalLayout_7.addWidget(self.createquiz_opt1_label)

        self.createquiz_opt1_lineedit = QLineEdit(self.opt1_frame)
        self.createquiz_opt1_lineedit.setObjectName(u"createquiz_opt1_lineedit")

        self.horizontalLayout_7.addWidget(self.createquiz_opt1_lineedit)


        self.verticalLayout_4.addWidget(self.opt1_frame)

        self.opt2_frame = QFrame(self.add_new_qs_frame)
        self.opt2_frame.setObjectName(u"opt2_frame")
        self.opt2_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.opt2_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.opt2_frame)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.createquiz_opt2_label = QLabel(self.opt2_frame)
        self.createquiz_opt2_label.setObjectName(u"createquiz_opt2_label")
        self.createquiz_opt2_label.setFont(font)

        self.horizontalLayout_6.addWidget(self.createquiz_opt2_label)

        self.createquiz_opt2_lineedit = QLineEdit(self.opt2_frame)
        self.createquiz_opt2_lineedit.setObjectName(u"createquiz_opt2_lineedit")

        self.horizontalLayout_6.addWidget(self.createquiz_opt2_lineedit)


        self.verticalLayout_4.addWidget(self.opt2_frame)

        self.opt3_frame = QFrame(self.add_new_qs_frame)
        self.opt3_frame.setObjectName(u"opt3_frame")
        self.opt3_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.opt3_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.opt3_frame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.createquiz_opt3_label = QLabel(self.opt3_frame)
        self.createquiz_opt3_label.setObjectName(u"createquiz_opt3_label")
        self.createquiz_opt3_label.setFont(font)

        self.horizontalLayout_4.addWidget(self.createquiz_opt3_label)

        self.createquiz_opt3_lineedit = QLineEdit(self.opt3_frame)
        self.createquiz_opt3_lineedit.setObjectName(u"createquiz_opt3_lineedit")

        self.horizontalLayout_4.addWidget(self.createquiz_opt3_lineedit)


        self.verticalLayout_4.addWidget(self.opt3_frame)

        self.btn_frame = QFrame(self.add_new_qs_frame)
        self.btn_frame.setObjectName(u"btn_frame")
        self.btn_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.btn_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_9 = QGridLayout(self.btn_frame)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.createquiz_add_qs_btn = QPushButton(self.btn_frame)
        self.createquiz_add_qs_btn.setObjectName(u"createquiz_add_qs_btn")
        self.createquiz_add_qs_btn.setMaximumSize(QSize(170, 16777215))
        font5 = QFont()
        font5.setPointSize(10)
        font5.setBold(True)
        self.createquiz_add_qs_btn.setFont(font5)

        self.gridLayout_9.addWidget(self.createquiz_add_qs_btn, 0, 1, 1, 1)

        self.show_all_qs_btn = QPushButton(self.btn_frame)
        self.show_all_qs_btn.setObjectName(u"show_all_qs_btn")
        self.show_all_qs_btn.setMaximumSize(QSize(130, 16777215))

        self.gridLayout_9.addWidget(self.show_all_qs_btn, 0, 2, 1, 1)

        self.btn_horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_9.addItem(self.btn_horizontalSpacer, 0, 3, 1, 1)


        self.verticalLayout_4.addWidget(self.btn_frame)


        self.gridLayout_3.addWidget(self.add_new_qs_frame, 0, 0, 1, 1)

        self.all_qs_frame = QFrame(self.createquiz_stackwidget_page)
        self.all_qs_frame.setObjectName(u"all_qs_frame")
        sizePolicy1.setHeightForWidth(self.all_qs_frame.sizePolicy().hasHeightForWidth())
        self.all_qs_frame.setSizePolicy(sizePolicy1)
        self.all_qs_frame.setStyleSheet(u"")
        self.all_qs_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.all_qs_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_7 = QGridLayout(self.all_qs_frame)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.all_qs_tableview = QTableView(self.all_qs_frame)
        self.all_qs_tableview.setObjectName(u"all_qs_tableview")
        self.all_qs_tableview.setStyleSheet(u"QTableView {\n"
"    border: 1px solid #e0e6ed;\n"
"    gridline-color: #f3f4f6;\n"
"    border-radius: 15px;\n"
"    background-color: white;\n"
"    selection-background-color: #ebf5fb; \n"
"    selection-color: #2980b9;\n"
"    alternate-background-color: #f8f9fa; \n"
"}\n"
"\n"
"QHeaderView::vertical {\n"
"    width: 0px;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #f8f9fa;\n"
"    color: #34495e;\n"
"    padding: 5px;\n"
"    font-weight: bold;\n"
"    border: none;\n"
"    border-bottom: 2px solid #3498db;\n"
"}")
        self.all_qs_tableview.horizontalHeader().setCascadingSectionResizes(True)
        self.all_qs_tableview.horizontalHeader().setProperty(u"showSortIndicator", False)
        self.all_qs_tableview.verticalHeader().setCascadingSectionResizes(True)

        self.gridLayout_7.addWidget(self.all_qs_tableview, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.all_qs_frame, 1, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer, 2, 0, 1, 1)

        self.homepage_stackwidget.addWidget(self.createquiz_stackwidget_page)
        self.results_stackwidget_page = QWidget()
        self.results_stackwidget_page.setObjectName(u"results_stackwidget_page")
        self.results_stackwidget_page.setStyleSheet(u"#result_summary_label {\n"
"    color: #1a2a6c;\n"
"    font-size: 24px;\n"
"    font-weight: bold;\n"
"    margin-bottom: 15px;\n"
"}\n"
"\n"
"\n"
"")
        self.gridLayout_2 = QGridLayout(self.results_stackwidget_page)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.result_tableview = QTableView(self.results_stackwidget_page)
        self.result_tableview.setObjectName(u"result_tableview")
        self.result_tableview.setStyleSheet(u"QTableView {\n"
"    background-color: white;\n"
"    alternate-background-color: #f8f9fa; \n"
"    selection-background-color: #d1ecf1;\n"
"    selection-color: #0c5460;\n"
"    gridline-color: #dee2e6;\n"
"    border: 1px solid #dee2e6;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #f1f1f1;\n"
"    padding: 6px;\n"
"    border: 1px solid #dee2e6;\n"
"    font-weight: bold;\n"
"}")
        self.result_tableview.setSortingEnabled(True)
        self.result_tableview.horizontalHeader().setCascadingSectionResizes(True)
        self.result_tableview.horizontalHeader().setProperty(u"showSortIndicator", True)

        self.gridLayout_2.addWidget(self.result_tableview, 1, 0, 1, 1)

        self.result_summary_label = QLabel(self.results_stackwidget_page)
        self.result_summary_label.setObjectName(u"result_summary_label")
        font6 = QFont()
        font6.setFamilies([u"Arial"])
        font6.setBold(True)
        font6.setUnderline(True)
        self.result_summary_label.setFont(font6)

        self.gridLayout_2.addWidget(self.result_summary_label, 0, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.homepage_stackwidget.addWidget(self.results_stackwidget_page)

        self.horizontalLayout.addWidget(self.homepage_stackwidget)

        self.mainStackWidget.addWidget(self.home_page)

        self.verticalLayout.addWidget(self.mainStackWidget)

        Home.setCentralWidget(self.homeWidget)

        self.retranslateUi(Home)

        self.mainStackWidget.setCurrentIndex(1)
        self.createquiz_sidebar_btn_home.setDefault(False)
        self.homepage_stackwidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Home)
    # setupUi

    def retranslateUi(self, Home):
        Home.setWindowTitle(QCoreApplication.translate("Home", u"SmartGrading", None))
        self.signup_btn_login.setText(QCoreApplication.translate("Home", u"Sign Up", None))
        self.username_label_login.setText(QCoreApplication.translate("Home", u"Username:", None))
        self.login_btn_login.setText(QCoreApplication.translate("Home", u"Login", None))
        self.password_label_login.setText(QCoreApplication.translate("Home", u"Password:", None))
        self.password_lineedit_login.setText("")
        self.welcome_label_login.setText(QCoreApplication.translate("Home", u"Welcome to SmartGrading!", None))
        self.subtitle_label_login.setText(QCoreApplication.translate("Home", u"Please Login or Sign Up to continue.", None))
        self.menu_sidebar_label_home.setText(QCoreApplication.translate("Home", u"Menu", None))
        self.createquiz_sidebar_btn_home.setText(QCoreApplication.translate("Home", u"Create Quiz", None))
        self.attendquiz_sidebar_btn_home.setText(QCoreApplication.translate("Home", u"Attend Quiz", None))
        self.results_sidebar_btn_home.setText(QCoreApplication.translate("Home", u"Results", None))
        self.logout_sidebar_btn_home.setText(QCoreApplication.translate("Home", u"Log Out", None))
        self.start_quiz_btn.setText(QCoreApplication.translate("Home", u"Start Quiz", None))
        self.select_qs_number_label.setText(QCoreApplication.translate("Home", u"Select Number of question :", None))
        self.quiz_qs_label.setText(QCoreApplication.translate("Home", u"Question", None))
        self.qs_opt0_radio.setText(QCoreApplication.translate("Home", u"Option 0", None))
        self.qs_opt1_radio.setText(QCoreApplication.translate("Home", u"Option 1", None))
        self.qs_opt2_radio.setText(QCoreApplication.translate("Home", u"Option 2", None))
        self.qs_opt3_radio.setText(QCoreApplication.translate("Home", u"Option 3", None))
        self.next_qs_btn.setText(QCoreApplication.translate("Home", u"Next", None))
        self.restart_quiz_btn.setText(QCoreApplication.translate("Home", u"Restart Quiz", None))
        self.show_result_label.setText(QCoreApplication.translate("Home", u"You got x marks!", None))
        self.add_new_qs_label.setText(QCoreApplication.translate("Home", u"Create New Question", None))
        self.createquiz_qs_label.setText(QCoreApplication.translate("Home", u"Question:", None))
        self.createquiz_ans_label.setText(QCoreApplication.translate("Home", u"Answer:  ", None))
        self.createquiz_other_option_label.setText(QCoreApplication.translate("Home", u"Other Options:", None))
        self.createquiz_opt1_label.setText(QCoreApplication.translate("Home", u"Option 1:", None))
        self.createquiz_opt2_label.setText(QCoreApplication.translate("Home", u"Option 2:", None))
        self.createquiz_opt3_label.setText(QCoreApplication.translate("Home", u"Option 3:", None))
        self.createquiz_add_qs_btn.setText(QCoreApplication.translate("Home", u"Add Question", None))
        self.show_all_qs_btn.setText(QCoreApplication.translate("Home", u"Show All Questions", None))
        self.result_summary_label.setText(QCoreApplication.translate("Home", u"Assessment Results Summary", None))
    # retranslateUi

