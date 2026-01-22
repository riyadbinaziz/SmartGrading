from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow
from studentHome.ui_studentHome import Ui_MainWindow

class studentHome(QMainWindow, Ui_MainWindow):
    def __init__ (self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Home")
        