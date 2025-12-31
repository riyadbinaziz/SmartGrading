from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget
from login.ui_login import Ui_login

class login (QWidget, Ui_login):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Login Page")
        self.login_button.clicked.connect(self.do_something)

    def do_something(self):
        print("Congrats it works")