import sys
from PySide6 import QtWidgets
from login.login import login

app = QtWidgets.QApplication(sys.argv)

window = login()
window.show()

app.exec()