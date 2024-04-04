import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QVBoxLayout, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Display Text from External File")
        self.setGeometry(100, 100, 400, 300)

        # Text Edit
        self.text_edit = QTextEdit()

        # Read text from external file
        filename = r"C:\Users\Daksh Chhabra\Downloads\pyqt5_projects\texteditor_pyqt5\hello.txt"
        try:
            with open(filename, 'r') as file:
                text = file.read()
                self.text_edit.setPlainText(text)
        except FileNotFoundError:
            print(f"File '{filename}' not found.")

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.text_edit)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())

