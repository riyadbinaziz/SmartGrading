from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtCore import Qt

class ResultPageHandler:
    def __init__(self, ui, db, main_window):
        """
        Initializes the handler for the Assessment Results Summary page.
        """
        self.ui = ui
        self.db = db
        self.main_window = main_window

    def load_user_results(self):
        """
        Fetches the current user's quiz history and displays it in the table view
        with automatic row numbering (Sl No.) on the far left.
        """
        # 1. Get the current logged-in user ID
        user_id = self.main_window.current_user_id
        
        if user_id is None:
            return

        # 2. Fetch history data from the database
        # Expected row_data format: (correct_answers, total_questions, percentage, date_taken)
        history = self.db.get_user_history(user_id)

        # 3. Create a Table Model with 4 columns (data columns only)
        # The row numbering is handled by the TableView's vertical header
        model = QStandardItemModel(len(history), 4)
        
        # Define headers for the assessment data
        model.setHorizontalHeaderLabels([
            "Correctly Answered", 
            "Total Questions", 
            "Percentage", 
            "Date Taken"
        ])

        # 4. Fill the model with database data
        for row_idx, row_data in enumerate(history):
            for db_col_idx, value in enumerate(row_data):
                # Format the percentage column specifically
                if db_col_idx == 2:
                    item_text = f"{value}%"
                else:
                    item_text = str(value)
                
                # Create the table item and center the text
                item = QStandardItem(item_text)
                item.setTextAlignment(Qt.AlignCenter)
                
                # Map the database column directly to the model column
                model.setItem(row_idx, db_col_idx, item)

        # 5. Apply the model to your specific widget
        self.ui.result_tableview.setModel(model)
        
        # --- UI Polish ---
        
        # Enable the vertical header to show automatic 1, 2, 3... numbering
        self.ui.result_tableview.verticalHeader().setVisible(True)
        
        # Configure horizontal header behavior
        header = self.ui.result_tableview.horizontalHeader()
        
        # Stretch the last column (Date Taken) to fill remaining space
        header.setStretchLastSection(True)
        
        # Resize columns to fit the content of the data
        self.ui.result_tableview.resizeColumnsToContents()