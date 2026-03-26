from PySide6.QtWidgets import QMessageBox

class AuthHandler:
    def __init__(self, ui, db, main_window):
        self.ui = ui
        self.db = db
        self.main_window = main_window

        # Connecting buttons using your exact object names
        self.ui.signup_btn_login.clicked.connect(self.handle_signup)
        self.ui.login_btn_login.clicked.connect(self.handle_login)

    def handle_signup(self):
        username = self.ui.username_lineedit_login.text().strip()
        password = self.ui.password_lineedit_login.text().strip()

        if not username or not password:
            QMessageBox.warning(None, "Input Error", "Please fill in all fields.")
            return

        # Attempt to add to database
        success = self.db.add_user(username, password)

        if success:
            QMessageBox.information(None, "Success", "Account Created Successfully!")
            
            # Auto-login after signup
            user_data = self.db.check_user(username, password)
            if user_data:
                self.main_window.current_user_id = user_data[0]
                # Switch to home_page then the attend quiz sub-page
                self.ui.mainStackWidget.setCurrentWidget(self.ui.home_page)
                self.ui.homepage_stackwidget.setCurrentWidget(self.ui.attendquiz_stackwidget_page)
        else:
            QMessageBox.critical(None, "Error", "Username already exists!")

    def handle_login(self):
        username = self.ui.username_lineedit_login.text().strip()
        password = self.ui.password_lineedit_login.text().strip()

        user_data = self.db.check_user(username, password)

        if user_data:
            self.main_window.current_user_id = user_data[0]
            QMessageBox.information(None, "Login Success", f"Welcome back, {username}!")
            
            # Navigation logic for your nested stacks
            self.ui.mainStackWidget.setCurrentWidget(self.ui.home_page)
            self.ui.homepage_stackwidget.setCurrentWidget(self.ui.attendquiz_stackwidget_page)
        else:
            QMessageBox.critical(None, "Login Failed", "Invalid username or password.")

    def clear_fields(self):
        self.ui.username_lineedit_login.clear()
        self.ui.password_lineedit_login.clear()