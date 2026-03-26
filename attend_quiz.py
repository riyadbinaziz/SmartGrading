import random
from PySide6.QtWidgets import QMessageBox

class AttendQuizHandler:
    def __init__(self, ui, db, main_window):
        self.ui = ui
        self.db = db
        self.main_window = main_window
        
        # State management
        self.quiz_questions = []
        self.current_q_index = 0
        self.user_score = 0
        self.correct_answer_text = ""

        # Initial UI State
        self.prepare_initial_state()

        # Connect Buttons
        self.ui.start_quiz_btn.clicked.connect(self.start_quiz_session)
        self.ui.next_qs_btn.clicked.connect(self.process_next_step)
        self.ui.restart_quiz_btn.clicked.connect(self.prepare_initial_state)

    def prepare_initial_state(self):
        """Shows only the selection frame and resets the spinbox range."""
        self.ui.select_qs_number_frame.show()
        self.ui.quiz_qs_frame.hide()
        self.ui.show_result_frame.hide()
        
        # Set spinbox limits based on database content
        total_available = self.db.get_total_question_count()
        self.ui.select_qs_number_spinbox.setMinimum(1)
        self.ui.select_qs_number_spinbox.setMaximum(max(1, total_available))

    def start_quiz_session(self):
        """Transitions to the quiz frame and loads random questions."""
        count = self.ui.select_qs_number_spinbox.value()
        self.quiz_questions = self.db.get_random_questions(count)

        if not self.quiz_questions:
            QMessageBox.warning(None, "No Questions", "Please add questions to the database first.")
            return

        self.user_score = 0
        self.current_q_index = 0
        
        self.ui.select_qs_number_frame.hide()
        self.ui.quiz_qs_frame.show()
        self.display_current_question()

    def display_current_question(self):
        """Displays text and shuffles options for the radio buttons."""
        # data format: (id, question_text, correct_answer, opt1, opt2, opt3)
        q_data = self.quiz_questions[self.current_q_index]
        self.ui.quiz_qs_label.setText(q_data[1])
        
        self.correct_answer_text = q_data[2]
        
        # Randomize the order of all 4 options
        options = [q_data[2], q_data[3], q_data[4], q_data[5]]
        random.shuffle(options)

        # Assign text to radio buttons
        self.ui.qs_opt0_radio.setText(options[0])
        self.ui.qs_opt1_radio.setText(options[1])
        self.ui.qs_opt2_radio.setText(options[2])
        self.ui.qs_opt3_radio.setText(options[3])

        # Reset radio selection visually
        self.ui.quiz_qs_frame_btngrp.setExclusive(False)
        for btn in [self.ui.qs_opt0_radio, self.ui.qs_opt1_radio, self.ui.qs_opt2_radio, self.ui.qs_opt3_radio]:
            btn.setChecked(False)
        self.ui.quiz_qs_frame_btngrp.setExclusive(True)

    def process_next_step(self):
        """Checks the answer and moves to next question or results."""
        selected_btn = self.ui.quiz_qs_frame_btngrp.checkedButton()
        
        if not selected_btn:
            QMessageBox.warning(None, "Selection Required", "Please select an answer.")
            return

        if selected_btn.text() == self.correct_answer_text:
            self.user_score += 1

        self.current_q_index += 1
        
        if self.current_q_index < len(self.quiz_questions):
            self.display_current_question()
        else:
            self.finalize_quiz()

    def finalize_quiz(self):
        """Shows results and saves score to the database."""
        self.ui.quiz_qs_frame.hide()
        self.ui.show_result_frame.show()
        
        total = len(self.quiz_questions)
        self.ui.show_result_label.setText(f"Congratulations! You got {self.user_score} marks.")
        
        # Save results to database per user
        self.db.save_quiz_result(self.main_window.current_user_id, self.user_score, total)