from PySide6.QtWidgets import QMessageBox
from PySide6.QtGui import QStandardItemModel, QStandardItem

class CreateQuizHandler:
    def __init__(self, ui, db):
        self.ui = ui
        self.db = db

        # 1. Hide the "all question frame" by default
        self.ui.all_qs_frame.hide()

        # 2. Connect Buttons (Names from image_15c0d4.png and image_15c3a3.png)
        self.ui.createquiz_add_qs_btn.clicked.connect(self.add_question_to_db)
        self.ui.show_all_qs_btn.clicked.connect(self.toggle_all_questions_view)

    def add_question_to_db(self):
        """Extracts text and saves to the database fields."""
        # Extracting text from your specific lineedit names
        question_text = self.ui.createquiz_qs_lineedit.text().strip()
        correct_answer = self.ui.createquiz_ans_lineedit.text().strip()
        opt1 = self.ui.createquiz_opt1_lineedit.text().strip()
        opt2 = self.ui.createquiz_opt2_lineedit.text().strip()
        opt3 = self.ui.createquiz_opt3_lineedit.text().strip()

        # Validation: Check if all info is provided
        if not all([question_text, correct_answer, opt1, opt2, opt3]):
            QMessageBox.warning(None, "Input Error", "Please fill in all fields before adding a question.")
            return

        # Add to database using the fields specified
        self.db.add_question(question_text, correct_answer, opt1, opt2, opt3)
        
        QMessageBox.information(None, "Success", "Question added successfully to the database!")
        
        # Clear fields for the next entry
        self.clear_input_fields()

    def toggle_all_questions_view(self):
        """Toggles the frame visibility and refreshes the table."""
        if self.ui.all_qs_frame.isVisible():
            self.ui.all_qs_frame.hide()
        else:
            self.ui.all_qs_frame.show()
            self.load_questions_to_table()

    def load_questions_to_table(self):
        """Displays data in the tableview safely."""
        questions = self.db.get_all_questions() 
    
        # Define model: Rows = len(questions), Columns = 5
        model = QStandardItemModel(len(questions), 5)
        model.setHorizontalHeaderLabels(["Question", "Answer", "Option 1", "Option 2", "Option 3"])

        for row_idx, row_data in enumerate(questions):
        # row_data is a tuple: (id, text, ans, opt1, opt2, opt3)
        # We map them manually to avoid index errors:
            model.setItem(row_idx, 0, QStandardItem(str(row_data[1]))) # Text
            model.setItem(row_idx, 1, QStandardItem(str(row_data[2]))) # Answer
            model.setItem(row_idx, 2, QStandardItem(str(row_data[3]))) # Opt 1
            model.setItem(row_idx, 3, QStandardItem(str(row_data[4]))) # Opt 2
            model.setItem(row_idx, 4, QStandardItem(str(row_data[5]))) # Opt 3

        self.ui.all_qs_tableview.setModel(model)
        self.ui.all_qs_tableview.resizeColumnsToContents()

    def clear_input_fields(self):
        self.ui.createquiz_qs_lineedit.clear()
        self.ui.createquiz_ans_lineedit.clear()
        self.ui.createquiz_opt1_lineedit.clear()
        self.ui.createquiz_opt2_lineedit.clear()
        self.ui.createquiz_opt3_lineedit.clear()