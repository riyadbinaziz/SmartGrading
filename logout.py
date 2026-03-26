class LogoutHandler:
    def __init__(self, ui, main_window, auth_handler, attend_quiz_logic):
        self.ui = ui
        self.main_window = main_window
        self.auth_handler = auth_handler
        self.attend_quiz_logic = attend_quiz_logic # New dependency
        
        self.ui.logout_sidebar_btn_home.clicked.connect(self.handle_logout)

    def handle_logout(self):
        """Clears session and resets the quiz UI for the next user."""
        # 1. Clear session
        self.main_window.current_user_id = None
        
        # 2. Reset Login Fields
        self.auth_handler.clear_fields()
        
        # 3. RESET ATTEND QUIZ STATE
        # This ensures the spinbox is visible and set to 1
        self.attend_quiz_logic.prepare_initial_state()
        
        # 4. Redirect to login
        self.ui.mainStackWidget.setCurrentWidget(self.ui.login_page)