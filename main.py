import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from ui_main import Ui_Home
from database import QuizDatabase
from auth import AuthHandler
from create_quiz import CreateQuizHandler

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

        # --- Sidebar Navigation Logic ---
        # Based on image_b3a022.png names
        self.ui.attendquiz_sidebar_btn_home.clicked.connect(
            lambda: self.ui.homepage_stackwidget.setCurrentWidget(self.ui.attendquiz_stackwidget_page)
        )
        self.ui.createquiz_sidebar_btn_home.clicked.connect(
            lambda: self.ui.homepage_stackwidget.setCurrentWidget(self.ui.createquiz_stackwidget_page)
        )
        self.ui.results_sidebar_btn_home.clicked.connect(
            lambda: self.ui.homepage_stackwidget.setCurrentWidget(self.ui.results_stackwidget_page)
        )
        
        # Exit Button
        self.ui.exit_sidebar_btn_home.clicked.connect(self.close)

        # Ensure we start on the login page
        self.ui.mainStackWidget.setCurrentWidget(self.ui.login_page)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyQuizApp()
    window.show()
    sys.exit(app.exec())