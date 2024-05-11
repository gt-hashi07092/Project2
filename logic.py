import csv
import random
from datetime import datetime, timedelta
from PyQt6.QtWidgets import QApplication, QMainWindow
from appdesign import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.call_it_a_day)

        # quotes.csvからランダムな引用とその作者名を取得
        self.quotes = []
        with open('quotes.csv', newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='"')
            for row in reader:
                self.quotes.append(row)
        self.display_random_quote()
        
        self.diary_file_path = "diary.csv"
        #we can change file path right here
        
        # last_entry_dateとstreak_countを初期化
        self.last_entry_date = None
        self.streak_count = 0

    def display_random_quote(self):
        quote, author = random.choice(self.quotes)
        self.ui.label_quote.setText(f'{quote}')
        self.ui.label_quote_name.setText(f"-{author}")

    def call_it_a_day(self):
        what_happened = self.ui.plainTextEdit_what_happened.toPlainText()
        day_rating = self.ui.comboBox_grade.currentText()

        # 日付を取得
        today = datetime.now().date()
        
        # ストリークカウントを更新
        if self.last_entry_date is None or today == self.last_entry_date + timedelta(days=1):
            self.streak_count += 1
        else:
            self.streak_count = 1
        self.last_entry_date = today

        # CSVファイルに書き込む
        with open(self.diary_file_path, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([today, what_happened, day_rating])
        
        # ストリーク表示を更新
        self.ui.label_streak_days.setText(str(self.streak_count))
        #save完了のメッセージ
        self.ui.label_haveagreatnight.setText("Saved! Have a great Night :)")