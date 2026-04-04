import sys
from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow
from ui_main import Ui_Home
from database import QuizDatabase
from auth import AuthHandler
from create_quiz import CreateQuizHandler
from result_page import ResultPageHandler
from attend_quiz import AttendQuizHandler
from logout import LogoutHandler

class MyQuizApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Home()
        self.ui.setupUi(self)

        # imports classes from other files
        self.db = QuizDatabase()
        self.current_user_id = None
        self.auth = AuthHandler(self.ui, self.db, self)
        self.create_quiz_logic = CreateQuizHandler(self.ui, self.db)
        self.attend_quiz_logic = AttendQuizHandler(self.ui, self.db, self)
        self.result_logic = ResultPageHandler(self.ui, self.db, self)
        self.logout_logic = LogoutHandler(self.ui, self, self.auth, self.attend_quiz_logic)

        # Sidebar button connect
        self.ui.attendquiz_sidebar_btn_home.clicked.connect(self.navigate_to_attend_quiz)

        self.ui.createquiz_sidebar_btn_home.clicked.connect(
            lambda: self.ui.homepage_stackwidget.setCurrentWidget(self.ui.createquiz_stackwidget_page)
        )

        self.ui.results_sidebar_btn_home.clicked.connect(self.navigate_to_results)

        self.ui.logout_sidebar_btn_home.clicked.connect(self.logout_logic.handle_logout)

        self.ui.mainStackWidget.setCurrentWidget(self.ui.login_page)

        self.ui.all_qs_tableview.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

    # takes to the results page
    def navigate_to_results(self):
        self.ui.homepage_stackwidget.setCurrentWidget(self.ui.results_stackwidget_page)
        self.result_logic.load_user_results()

    # takes to attend quiz page
    def navigate_to_attend_quiz(self):
        self.ui.homepage_stackwidget.setCurrentWidget(self.ui.attendquiz_stackwidget_page)
        self.attend_quiz_logic.prepare_initial_state()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyQuizApp()
    window.show()
    sys.exit(app.exec())