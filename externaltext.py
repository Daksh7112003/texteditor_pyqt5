import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QPushButton, QVBoxLayout, QWidget, QInputDialog

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("External Input Example")
        self.setGeometry(100, 100, 400, 300)

        # Text Edit
        self.text_edit = QTextEdit()

        # Button to take external input
        self.button = QPushButton("Take External Input")
        self.button.clicked.connect(self.take_external_input)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.button)
        layout.addWidget(self.text_edit)

        container = QWidget()


        container.setLayout(layout)


        self.setCentralWidget(container)



    def take_external_input(self):
    
        text, ok = QInputDialog.getText(self, "Input", "Enter your text:")
        if ok and text.strip():
              # Only append if the input is not empty
            self.text_edit.append(text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
