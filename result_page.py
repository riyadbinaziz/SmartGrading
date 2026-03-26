from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtCore import Qt

class ResultPageHandler:
    def __init__(self, ui, db, main_window):
        self.ui = ui
        self.db = db
        self.main_window = main_window

    def load_user_results(self):
        """Fetches and displays the current user's quiz history with a Serial No."""
        user_id = self.main_window.current_user_id
        
        if user_id is None:
            return

        # 1. Fetch data from database
        history = self.db.get_user_history(user_id)

        # 2. Create the Table Model
        # Increased to 5 columns to accommodate the Serial No.
        model = QStandardItemModel(len(history), 5)
        
        # Setting custom headers with Serial No. on the far left
        model.setHorizontalHeaderLabels([
            "Sl No.",
            "Correctly Answered", 
            "Total Questions", 
            "Percentage", 
            "Date Taken"
        ])

        # 3. Fill the model with data
        for row_idx, row_data in enumerate(history):
            # Add Serial Number to the first column (col_idx 0)
            sl_no_item = QStandardItem(str(row_idx + 1))
            sl_no_item.setTextAlignment(Qt.AlignCenter)
            model.setItem(row_idx, 0, sl_no_item)

            # Fill remaining data from database into columns 1-4
            for db_col_idx, value in enumerate(row_data):
                if db_col_idx == 2:  # Percentage formatting
                    item_text = f"{value}%"
                else:
                    item_text = str(value)
                
                item = QStandardItem(item_text)
                item.setTextAlignment(Qt.AlignCenter)
                # Shift database data by 1 column to make room for Sl No.
                model.setItem(row_idx, db_col_idx + 1, item)

        # 4. Apply the model to your specific widget name
        self.ui.result_tableview.setModel(model)
        
        # UI Polish
        header = self.ui.result_tableview.horizontalHeader()
        header.setStretchLastSection(True)
        self.ui.result_tableview.resizeColumnsToContents()