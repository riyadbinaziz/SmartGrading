class LogoutHandler:
    def __init__(self, ui, main_window, auth_handler, attend_quiz_logic):
        self.ui = ui
        self.main_window = main_window
        self.auth_handler = auth_handler
        self.attend_quiz_logic = attend_quiz_logic 
        self.ui.logout_sidebar_btn_home.clicked.connect(self.handle_logout)

    # does stuff when logout btn is clicked
    def handle_logout(self):
        self.main_window.current_user_id = None
        self.auth_handler.clear_fields()
        self.attend_quiz_logic.prepare_initial_state()
        self.ui.mainStackWidget.setCurrentWidget(self.ui.login_page)