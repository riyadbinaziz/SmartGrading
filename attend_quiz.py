import random
from PySide6.QtWidgets import QMessageBox

class AttendQuizHandler:
    def __init__(self, ui, db, main_window):
        self.ui = ui
        self.db = db
        self.main_window = main_window
        
        # initial State setup
        self.quiz_questions = []
        self.current_q_index = 0
        self.user_score = 0
        self.correct_answer_text = ""

        self.prepare_initial_state()

        # button connections
        self.ui.start_quiz_btn.clicked.connect(self.start_quiz_session)
        self.ui.next_qs_btn.clicked.connect(self.process_next_step)
        self.ui.restart_quiz_btn.clicked.connect(self.prepare_initial_state)

    # makes the page fresh again
    def prepare_initial_state(self):
        self.ui.select_qs_number_frame.show()
        self.ui.quiz_qs_frame.hide()
        self.ui.show_result_frame.hide()
    
        self.ui.select_qs_number_spinbox.setValue(1)
    
        count = self.db.get_question_count()
        self.ui.select_qs_number_spinbox.setMaximum(count)

    # quiz page starts
    def start_quiz_session(self):
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

    # shuffling the options
    def display_current_question(self):
        q_data = self.quiz_questions[self.current_q_index]
        self.ui.quiz_qs_label.setText(q_data[1])
        
        self.correct_answer_text = q_data[2]
        
        options = [q_data[2], q_data[3], q_data[4], q_data[5]]
        random.shuffle(options)

        self.ui.qs_opt0_radio.setText(options[0])
        self.ui.qs_opt1_radio.setText(options[1])
        self.ui.qs_opt2_radio.setText(options[2])
        self.ui.qs_opt3_radio.setText(options[3])

        self.ui.quiz_qs_frame_btngrp.setExclusive(False)
        for btn in [self.ui.qs_opt0_radio, self.ui.qs_opt1_radio, self.ui.qs_opt2_radio, self.ui.qs_opt3_radio]:
            btn.setChecked(False)
        self.ui.quiz_qs_frame_btngrp.setExclusive(True)

    # moving to next question
    def process_next_step(self):
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

    # show, save result to the database
    def finalize_quiz(self):
        self.ui.quiz_qs_frame.hide()
        self.ui.show_result_frame.show()
        
        total = len(self.quiz_questions)
        self.ui.show_result_label.setText(f"Congratulations! You got {self.user_score} marks.")
        
        self.db.save_quiz_result(self.main_window.current_user_id, self.user_score, total)