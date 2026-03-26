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
        Home.resize(657, 551)
        self.homeWidget = QWidget(Home)
        self.homeWidget.setObjectName(u"homeWidget")
        self.verticalLayout = QVBoxLayout(self.homeWidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.mainStackWidget = QStackedWidget(self.homeWidget)
        self.mainStackWidget.setObjectName(u"mainStackWidget")
        self.login_page = QWidget()
        self.login_page.setObjectName(u"login_page")
        self.gridLayout = QGridLayout(self.login_page)
        self.gridLayout.setObjectName(u"gridLayout")
        self.password_label_login = QLabel(self.login_page)
        self.password_label_login.setObjectName(u"password_label_login")
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.password_label_login.setFont(font)

        self.gridLayout.addWidget(self.password_label_login, 4, 1, 1, 1)

        self.username_label_login = QLabel(self.login_page)
        self.username_label_login.setObjectName(u"username_label_login")
        self.username_label_login.setFont(font)

        self.gridLayout.addWidget(self.username_label_login, 3, 1, 1, 1)

        self.horizontalspacer_login_above = QSpacerItem(158, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalspacer_login_above, 4, 5, 1, 1)

        self.login_btn_login = QPushButton(self.login_page)
        self.login_btn_login.setObjectName(u"login_btn_login")

        self.gridLayout.addWidget(self.login_btn_login, 5, 3, 1, 2)

        self.username_lineedit_login = QLineEdit(self.login_page)
        self.username_lineedit_login.setObjectName(u"username_lineedit_login")

        self.gridLayout.addWidget(self.username_lineedit_login, 3, 2, 1, 3)

        self.verticalapacer_login_below = QSpacerItem(20, 230, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalapacer_login_below, 6, 3, 1, 1)

        self.horizontalspacer_login_below = QSpacerItem(158, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalspacer_login_below, 4, 0, 1, 1)

        self.welcome_label_login = QLabel(self.login_page)
        self.welcome_label_login.setObjectName(u"welcome_label_login")
        font1 = QFont()
        font1.setPointSize(20)
        font1.setBold(True)
        self.welcome_label_login.setFont(font1)

        self.gridLayout.addWidget(self.welcome_label_login, 2, 2, 1, 2)

        self.password_lineedit_login = QLineEdit(self.login_page)
        self.password_lineedit_login.setObjectName(u"password_lineedit_login")

        self.gridLayout.addWidget(self.password_lineedit_login, 4, 2, 1, 3)

        self.verticalspacer_login_above = QSpacerItem(20, 213, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalspacer_login_above, 0, 3, 1, 1)

        self.signup_btn_login = QPushButton(self.login_page)
        self.signup_btn_login.setObjectName(u"signup_btn_login")

        self.gridLayout.addWidget(self.signup_btn_login, 5, 1, 1, 2)

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
        self.sidebar_frame_home.setFrameShape(QFrame.Shape.StyledPanel)
        self.sidebar_frame_home.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.sidebar_frame_home)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.menu_sidebar_label_home = QLabel(self.sidebar_frame_home)
        self.menu_sidebar_label_home.setObjectName(u"menu_sidebar_label_home")
        font2 = QFont()
        font2.setPointSize(15)
        font2.setBold(True)
        self.menu_sidebar_label_home.setFont(font2)

        self.verticalLayout_2.addWidget(self.menu_sidebar_label_home)

        self.createquiz_sidebar_btn_home = QPushButton(self.sidebar_frame_home)
        self.createquiz_sidebar_btn_home.setObjectName(u"createquiz_sidebar_btn_home")
        self.createquiz_sidebar_btn_home.setAutoDefault(False)
        self.createquiz_sidebar_btn_home.setFlat(False)

        self.verticalLayout_2.addWidget(self.createquiz_sidebar_btn_home)

        self.attendquiz_sidebar_btn_home = QPushButton(self.sidebar_frame_home)
        self.attendquiz_sidebar_btn_home.setObjectName(u"attendquiz_sidebar_btn_home")

        self.verticalLayout_2.addWidget(self.attendquiz_sidebar_btn_home)

        self.results_sidebar_btn_home = QPushButton(self.sidebar_frame_home)
        self.results_sidebar_btn_home.setObjectName(u"results_sidebar_btn_home")

        self.verticalLayout_2.addWidget(self.results_sidebar_btn_home)

        self.logout_sidebar_btn_home = QPushButton(self.sidebar_frame_home)
        self.logout_sidebar_btn_home.setObjectName(u"logout_sidebar_btn_home")

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
        font3.setPointSize(10)
        self.select_qs_number_spinbox.setFont(font3)

        self.gridLayout_5.addWidget(self.select_qs_number_spinbox, 0, 1, 1, 1)

        self.start_quiz_btn = QPushButton(self.select_qs_number_frame)
        self.start_quiz_btn.setObjectName(u"start_quiz_btn")
        self.start_quiz_btn.setFont(font3)

        self.gridLayout_5.addWidget(self.start_quiz_btn, 1, 0, 1, 1, Qt.AlignmentFlag.AlignLeft)

        self.select_qs_number_label = QLabel(self.select_qs_number_frame)
        self.select_qs_number_label.setObjectName(u"select_qs_number_label")
        self.select_qs_number_label.setMaximumSize(QSize(250, 16777215))
        font4 = QFont()
        font4.setPointSize(11)
        font4.setBold(False)
        self.select_qs_number_label.setFont(font4)

        self.gridLayout_5.addWidget(self.select_qs_number_label, 0, 0, 1, 1, Qt.AlignmentFlag.AlignTop)


        self.verticalLayout_3.addWidget(self.select_qs_number_frame)

        self.quiz_qs_frame = QFrame(self.attendquiz_stackwidget_page)
        self.quiz_qs_frame.setObjectName(u"quiz_qs_frame")
        sizePolicy.setHeightForWidth(self.quiz_qs_frame.sizePolicy().hasHeightForWidth())
        self.quiz_qs_frame.setSizePolicy(sizePolicy)
        self.quiz_qs_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.quiz_qs_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_4 = QGridLayout(self.quiz_qs_frame)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.quiz_qs_label = QLabel(self.quiz_qs_frame)
        self.quiz_qs_label.setObjectName(u"quiz_qs_label")
        self.quiz_qs_label.setFont(font3)

        self.gridLayout_4.addWidget(self.quiz_qs_label, 0, 0, 1, 1)

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
        self.next_qs_btn.setFont(font3)

        self.gridLayout_4.addWidget(self.next_qs_btn, 5, 0, 1, 1, Qt.AlignmentFlag.AlignLeft)


        self.verticalLayout_3.addWidget(self.quiz_qs_frame)

        self.show_result_frame = QFrame(self.attendquiz_stackwidget_page)
        self.show_result_frame.setObjectName(u"show_result_frame")
        sizePolicy.setHeightForWidth(self.show_result_frame.sizePolicy().hasHeightForWidth())
        self.show_result_frame.setSizePolicy(sizePolicy)
        self.show_result_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.show_result_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_6 = QGridLayout(self.show_result_frame)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.restart_quiz_btn = QPushButton(self.show_result_frame)
        self.restart_quiz_btn.setObjectName(u"restart_quiz_btn")
        self.restart_quiz_btn.setMaximumSize(QSize(170, 16777215))
        self.restart_quiz_btn.setFont(font3)

        self.gridLayout_6.addWidget(self.restart_quiz_btn, 3, 0, 1, 1, Qt.AlignmentFlag.AlignLeft)

        self.show_result_label = QLabel(self.show_result_frame)
        self.show_result_label.setObjectName(u"show_result_label")
        font5 = QFont()
        font5.setPointSize(13)
        font5.setBold(True)
        self.show_result_label.setFont(font5)

        self.gridLayout_6.addWidget(self.show_result_label, 2, 0, 1, 1)

        self.show_result_frame_horizontalspacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_6.addItem(self.show_result_frame_horizontalspacer, 2, 1, 1, 1)


        self.verticalLayout_3.addWidget(self.show_result_frame)

        self.attendquiz_verticalspacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.attendquiz_verticalspacer)

        self.homepage_stackwidget.addWidget(self.attendquiz_stackwidget_page)
        self.createquiz_stackwidget_page = QWidget()
        self.createquiz_stackwidget_page.setObjectName(u"createquiz_stackwidget_page")
        self.gridLayout_3 = QGridLayout(self.createquiz_stackwidget_page)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.createquiz_other_option_label = QLabel(self.createquiz_stackwidget_page)
        self.createquiz_other_option_label.setObjectName(u"createquiz_other_option_label")
        font6 = QFont()
        font6.setPointSize(10)
        font6.setBold(False)
        self.createquiz_other_option_label.setFont(font6)

        self.gridLayout_3.addWidget(self.createquiz_other_option_label, 3, 0, 1, 1)

        self.createquiz_opt1_lineedit = QLineEdit(self.createquiz_stackwidget_page)
        self.createquiz_opt1_lineedit.setObjectName(u"createquiz_opt1_lineedit")

        self.gridLayout_3.addWidget(self.createquiz_opt1_lineedit, 4, 2, 1, 1)

        self.createquiz_opt3_lineedit = QLineEdit(self.createquiz_stackwidget_page)
        self.createquiz_opt3_lineedit.setObjectName(u"createquiz_opt3_lineedit")

        self.gridLayout_3.addWidget(self.createquiz_opt3_lineedit, 6, 2, 1, 1)

        self.createquiz_ans_lineedit = QLineEdit(self.createquiz_stackwidget_page)
        self.createquiz_ans_lineedit.setObjectName(u"createquiz_ans_lineedit")

        self.gridLayout_3.addWidget(self.createquiz_ans_lineedit, 2, 2, 1, 1)

        self.createquiz_opt1_label = QLabel(self.createquiz_stackwidget_page)
        self.createquiz_opt1_label.setObjectName(u"createquiz_opt1_label")
        self.createquiz_opt1_label.setFont(font3)

        self.gridLayout_3.addWidget(self.createquiz_opt1_label, 4, 0, 1, 1)

        self.createquiz_qs_label = QLabel(self.createquiz_stackwidget_page)
        self.createquiz_qs_label.setObjectName(u"createquiz_qs_label")
        self.createquiz_qs_label.setFont(font3)

        self.gridLayout_3.addWidget(self.createquiz_qs_label, 1, 0, 1, 1)

        self.createquiz_opt3_label = QLabel(self.createquiz_stackwidget_page)
        self.createquiz_opt3_label.setObjectName(u"createquiz_opt3_label")
        self.createquiz_opt3_label.setFont(font3)

        self.gridLayout_3.addWidget(self.createquiz_opt3_label, 6, 0, 1, 1)

        self.createquiz_opt2_lineedit = QLineEdit(self.createquiz_stackwidget_page)
        self.createquiz_opt2_lineedit.setObjectName(u"createquiz_opt2_lineedit")

        self.gridLayout_3.addWidget(self.createquiz_opt2_lineedit, 5, 2, 1, 1)

        self.add_new_qs_label = QLabel(self.createquiz_stackwidget_page)
        self.add_new_qs_label.setObjectName(u"add_new_qs_label")
        self.add_new_qs_label.setFont(font5)
        self.add_new_qs_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.add_new_qs_label, 0, 0, 1, 3)

        self.all_qs_frame = QFrame(self.createquiz_stackwidget_page)
        self.all_qs_frame.setObjectName(u"all_qs_frame")
        self.all_qs_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.all_qs_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_7 = QGridLayout(self.all_qs_frame)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.all_qs_label = QLabel(self.all_qs_frame)
        self.all_qs_label.setObjectName(u"all_qs_label")
        font7 = QFont()
        font7.setPointSize(11)
        font7.setBold(True)
        self.all_qs_label.setFont(font7)

        self.gridLayout_7.addWidget(self.all_qs_label, 0, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.all_qs_tableview = QTableView(self.all_qs_frame)
        self.all_qs_tableview.setObjectName(u"all_qs_tableview")

        self.gridLayout_7.addWidget(self.all_qs_tableview, 1, 0, 1, 1)


        self.gridLayout_3.addWidget(self.all_qs_frame, 8, 0, 1, 3)

        self.createquiz_ans_label = QLabel(self.createquiz_stackwidget_page)
        self.createquiz_ans_label.setObjectName(u"createquiz_ans_label")
        self.createquiz_ans_label.setFont(font3)

        self.gridLayout_3.addWidget(self.createquiz_ans_label, 2, 0, 1, 1)

        self.createquiz_opt2_label = QLabel(self.createquiz_stackwidget_page)
        self.createquiz_opt2_label.setObjectName(u"createquiz_opt2_label")
        self.createquiz_opt2_label.setFont(font3)

        self.gridLayout_3.addWidget(self.createquiz_opt2_label, 5, 0, 1, 1)

        self.show_all_qs_btn = QPushButton(self.createquiz_stackwidget_page)
        self.show_all_qs_btn.setObjectName(u"show_all_qs_btn")
        self.show_all_qs_btn.setMaximumSize(QSize(130, 16777215))

        self.gridLayout_3.addWidget(self.show_all_qs_btn, 7, 2, 1, 1)

        self.createquiz_add_qs_btn = QPushButton(self.createquiz_stackwidget_page)
        self.createquiz_add_qs_btn.setObjectName(u"createquiz_add_qs_btn")
        self.createquiz_add_qs_btn.setMaximumSize(QSize(170, 16777215))
        self.createquiz_add_qs_btn.setFont(font3)

        self.gridLayout_3.addWidget(self.createquiz_add_qs_btn, 7, 0, 1, 1)

        self.createquiz_qs_lineedit = QLineEdit(self.createquiz_stackwidget_page)
        self.createquiz_qs_lineedit.setObjectName(u"createquiz_qs_lineedit")

        self.gridLayout_3.addWidget(self.createquiz_qs_lineedit, 1, 2, 1, 1)

        self.createquiz_verticalspacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.createquiz_verticalspacer, 9, 0, 1, 3)

        self.homepage_stackwidget.addWidget(self.createquiz_stackwidget_page)
        self.results_stackwidget_page = QWidget()
        self.results_stackwidget_page.setObjectName(u"results_stackwidget_page")
        self.gridLayout_2 = QGridLayout(self.results_stackwidget_page)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.result_tableview = QTableView(self.results_stackwidget_page)
        self.result_tableview.setObjectName(u"result_tableview")

        self.gridLayout_2.addWidget(self.result_tableview, 1, 0, 1, 1)

        self.result_summary_label = QLabel(self.results_stackwidget_page)
        self.result_summary_label.setObjectName(u"result_summary_label")
        font8 = QFont()
        font8.setFamilies([u"Arial"])
        font8.setPointSize(14)
        font8.setBold(True)
        font8.setUnderline(True)
        self.result_summary_label.setFont(font8)

        self.gridLayout_2.addWidget(self.result_summary_label, 0, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.homepage_stackwidget.addWidget(self.results_stackwidget_page)

        self.horizontalLayout.addWidget(self.homepage_stackwidget)

        self.mainStackWidget.addWidget(self.home_page)

        self.verticalLayout.addWidget(self.mainStackWidget)

        Home.setCentralWidget(self.homeWidget)

        self.retranslateUi(Home)

        self.mainStackWidget.setCurrentIndex(1)
        self.createquiz_sidebar_btn_home.setDefault(False)
        self.homepage_stackwidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Home)
    # setupUi

    def retranslateUi(self, Home):
        Home.setWindowTitle(QCoreApplication.translate("Home", u"SmartGrading", None))
        self.password_label_login.setText(QCoreApplication.translate("Home", u"Password:", None))
        self.username_label_login.setText(QCoreApplication.translate("Home", u"Username:", None))
        self.login_btn_login.setText(QCoreApplication.translate("Home", u"Login", None))
        self.welcome_label_login.setText(QCoreApplication.translate("Home", u"Welcome!", None))
        self.password_lineedit_login.setText("")
        self.signup_btn_login.setText(QCoreApplication.translate("Home", u"Sign Up", None))
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
        self.createquiz_other_option_label.setText(QCoreApplication.translate("Home", u"Other Options:", None))
        self.createquiz_opt1_label.setText(QCoreApplication.translate("Home", u"Option 1:", None))
        self.createquiz_qs_label.setText(QCoreApplication.translate("Home", u"Question:", None))
        self.createquiz_opt3_label.setText(QCoreApplication.translate("Home", u"Option 3:", None))
        self.add_new_qs_label.setText(QCoreApplication.translate("Home", u"Add New Question", None))
        self.all_qs_label.setText(QCoreApplication.translate("Home", u"All Questions", None))
        self.createquiz_ans_label.setText(QCoreApplication.translate("Home", u"Answer:", None))
        self.createquiz_opt2_label.setText(QCoreApplication.translate("Home", u"Option 2:", None))
        self.show_all_qs_btn.setText(QCoreApplication.translate("Home", u"Show All Question", None))
        self.createquiz_add_qs_btn.setText(QCoreApplication.translate("Home", u"Add Question", None))
        self.result_summary_label.setText(QCoreApplication.translate("Home", u"Assessment Results Summary", None))
    # retranslateUi

