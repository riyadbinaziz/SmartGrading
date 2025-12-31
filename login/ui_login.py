# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_login(object):
    def setupUi(self, login):
        if not login.objectName():
            login.setObjectName(u"login")
        login.resize(604, 376)
        self.welocme_label_login = QLabel(login)
        self.welocme_label_login.setObjectName(u"welocme_label_login")
        self.welocme_label_login.setEnabled(True)
        self.welocme_label_login.setGeometry(QRect(220, 110, 118, 28))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.welocme_label_login.sizePolicy().hasHeightForWidth())
        self.welocme_label_login.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(19)
        font.setBold(True)
        self.welocme_label_login.setFont(font)
        self.welocme_label_login.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.login_button = QPushButton(login)
        self.login_button.setObjectName(u"login_button")
        self.login_button.setGeometry(QRect(240, 210, 75, 24))
        font1 = QFont()
        font1.setBold(True)
        self.login_button.setFont(font1)
        self.widget = QWidget(login)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(162, 146, 240, 60))
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.username_label_login = QLabel(self.widget)
        self.username_label_login.setObjectName(u"username_label_login")
        font2 = QFont()
        font2.setPointSize(14)
        font2.setBold(True)
        self.username_label_login.setFont(font2)

        self.gridLayout.addWidget(self.username_label_login, 0, 0, 1, 1)

        self.username_lineedit_login = QLineEdit(self.widget)
        self.username_lineedit_login.setObjectName(u"username_lineedit_login")

        self.gridLayout.addWidget(self.username_lineedit_login, 0, 1, 1, 1)

        self.password_label_login = QLabel(self.widget)
        self.password_label_login.setObjectName(u"password_label_login")
        self.password_label_login.setFont(font2)

        self.gridLayout.addWidget(self.password_label_login, 1, 0, 1, 1)

        self.password_lineedit_login = QLineEdit(self.widget)
        self.password_lineedit_login.setObjectName(u"password_lineedit_login")

        self.gridLayout.addWidget(self.password_lineedit_login, 1, 1, 1, 1)


        self.retranslateUi(login)

        QMetaObject.connectSlotsByName(login)
    # setupUi

    def retranslateUi(self, login):
        login.setWindowTitle(QCoreApplication.translate("login", u"Form", None))
        self.welocme_label_login.setText(QCoreApplication.translate("login", u"Welcome!", None))
        self.login_button.setText(QCoreApplication.translate("login", u"Login", None))
        self.username_label_login.setText(QCoreApplication.translate("login", u"Username :", None))
        self.username_lineedit_login.setText("")
        self.password_label_login.setText(QCoreApplication.translate("login", u"Password :", None))
    # retranslateUi

