import sqlite3

class QuizDatabase:
    def __init__(self, db_name="quiz_app.db"):
        self.conn = sqlite3.connect(db_name, check_same_thread=False)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        # 1. USERS
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL
            )
        ''')

        # 2. QUESTIONS 
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS questions (
                question_id INTEGER PRIMARY KEY AUTOINCREMENT,
                question_text TEXT NOT NULL,
                correct_answer TEXT NOT NULL,
                option1 TEXT NOT NULL,
                option2 TEXT NOT NULL,
                option3 TEXT NOT NULL
            )
        ''')

        # 3. RESULTS 
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS results (
                result_id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                score INTEGER NOT NULL,
                total_questions INTEGER NOT NULL,
                percentage REAL NOT NULL,
                date_taken DATETIME DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users (user_id)
            )
        ''')
        self.conn.commit()

    # --- USER FEATURES ---
    def add_user(self, username, password):
        try:
            self.cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
            self.conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False 

    def check_user(self, username, password):
        self.cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
        return self.cursor.fetchone()

    # --- QUESTION FEATURES ---
    def add_question(self, q_text, correct, opt1, opt2, opt3):
        self.cursor.execute(
            "INSERT INTO questions (question_text, correct_answer, option1, option2, option3) VALUES (?, ?, ?, ?, ?)",
            (q_text, correct, opt1, opt2, opt3)
        )
        self.conn.commit()

    def get_question_count(self):
        """Returns total number of questions available."""
        self.cursor.execute("SELECT COUNT(*) FROM questions")
        return self.cursor.fetchone()[0]

    def get_random_questions(self, limit):
        self.cursor.execute("SELECT * FROM questions ORDER BY RANDOM() LIMIT ?", (limit,))
        return self.cursor.fetchall()

    # --- RESULT FEATURES ---
    def save_quiz_result(self, user_id, score, total):
        percentage = round((score / total * 100), 2) if total > 0 else 0
        self.cursor.execute(
            "INSERT INTO results (user_id, score, total_questions, percentage) VALUES (?, ?, ?, ?)",
            (user_id, score, total, percentage)
        )
        self.conn.commit()

    def get_user_history(self, user_id):
        """Returns formatted history for the UI TableView."""
        # Using strftime to make the date look cleaner (e.g., 2026-03-26)
        query = """
            SELECT score, total_questions, percentage, strftime('%Y-%m-%d %H:%M', date_taken) 
            FROM results 
            WHERE user_id = ? 
            ORDER BY date_taken DESC
        """
        self.cursor.execute(query, (user_id,))
        return self.cursor.fetchall()

    def close(self):
        self.conn.close()