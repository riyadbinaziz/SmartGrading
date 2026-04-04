from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtCore import Qt

class ResultPageHandler:
    def __init__(self, ui, db, main_window):
        self.ui = ui
        self.db = db
        self.main_window = main_window

    # gets the user history from db
    def load_user_results(self):
        user_id = self.main_window.current_user_id
        
        if user_id is None:
            return

        history = self.db.get_user_history(user_id)

        model = QStandardItemModel(len(history), 4)

        model.setHorizontalHeaderLabels([
            "Correctly Answered", 
            "Total Questions", 
            "Percentage", 
            "Date Taken"
        ])

        for row_idx, row_data in enumerate(history):
            for db_col_idx, value in enumerate(row_data):
                if db_col_idx == 2:
                    item_text = f"{value}%"
                else:
                    item_text = str(value)
                
                item = QStandardItem(item_text)
                item.setTextAlignment(Qt.AlignCenter)
                
                model.setItem(row_idx, db_col_idx, item)

        self.ui.result_tableview.setModel(model)
        
        self.ui.result_tableview.verticalHeader().setVisible(True)
        
        header = self.ui.result_tableview.horizontalHeader()
        
        header.setStretchLastSection(True)
        
        self.ui.result_tableview.resizeColumnsToContents()