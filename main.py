import sys
import logic


            
        

if __name__ == "__main__":
    app = logic.QApplication(sys.argv)
    window = logic.MainWindow()
    window.show()
    sys.exit(app.exec())