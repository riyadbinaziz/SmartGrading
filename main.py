import sys
from PySide6 import QtWidgets
from login.login import login
from studentHome.studentHome import studentHome

app = QtWidgets.QApplication(sys.argv)

window = studentHome()
window.show()

app.exec()