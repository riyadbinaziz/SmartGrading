import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from ui_main import Ui_Home
from database import QuizDatabase
from auth import AuthHandler
from create_quiz import CreateQuizHandler
from result_page import ResultPageHandler
from attend_quiz import AttendQuizHandler

class MyQuizApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Home()
        self.ui.setupUi(self)

        # Initialize shared components
        self.db = QuizDatabase()
        self.current_user_id = None

        # Initialize Auth Handler
        self.auth = AuthHandler(self.ui, self.db, self)

        self.create_quiz_logic = CreateQuizHandler(self.ui, self.db)

        self.attend_quiz_logic = AttendQuizHandler(self.ui, self.db, self)

        self.result_logic = ResultPageHandler(self.ui, self.db, self)

        # --- Sidebar Navigation Logic ---

        # 1. Attend Quiz (Resets and switches)
        self.ui.attendquiz_sidebar_btn_home.clicked.connect(self.navigate_to_attend_quiz)

        # 2. Create Quiz
        self.ui.createquiz_sidebar_btn_home.clicked.connect(
            lambda: self.ui.homepage_stackwidget.setCurrentWidget(self.ui.createquiz_stackwidget_page)
        )

        # 3. Results (Refreshes and switches)
        self.ui.results_sidebar_btn_home.clicked.connect(self.navigate_to_results)

        # 4. Log Out (Returns to login and clears user session)
        self.ui.logout_sidebar_btn_home.clicked.connect(self.handle_logout)

        # Ensure we start on the login page
        self.ui.mainStackWidget.setCurrentWidget(self.ui.login_page)

    # This function should be a method of your MyQuizApp class (properly indented)
    def navigate_to_results(self):
        # Switch the inner stack to results
        self.ui.homepage_stackwidget.setCurrentWidget(self.ui.results_stackwidget_page)
        # Call the load function from your results handler
        self.result_logic.load_user_results()

    def navigate_to_attend_quiz(self):
    """Resets the quiz UI to the selection frame and switches page."""
    # Switch the inner stack to Attend Quiz page
    self.ui.homepage_stackwidget.setCurrentWidget(self.ui.attendquiz_stackwidget_page)
    # Call the reset function from your attend quiz handler
    self.attend_quiz_logic.prepare_initial_state()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyQuizApp()
    window.show()
    sys.exit(app.exec())