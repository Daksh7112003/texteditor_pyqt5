# import os

# # Get the current working directory
# current_dir = os.getcwd()
# print("Current working directory:", current_dir)

# # Construct the file path relative to the current working directory
# filename = os.path.join(current_dir, 'japan.txt')
# print("Constructed file path:", filename)



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

        # Construct file path
        filename = 'japan.txt' 
        file_path = 'C:\\Users\\Daksh Chhabra\\Downloads\\pyqt5_projects\\' + filename

        try:
            # Read text from external file
            with open(file_path, 'r') as file:
                text = file.read()
                self.text_edit.setPlainText(text)
        except FileNotFoundError:
            print(f"File '{filename}' not found.")
        except Exception as e:
            print(f"Error reading file: {e}")
        
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
