import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QTextEdit, QWidget
import serial

class SerialReader(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Serial Reader")

        # Create QTextEdit widget to display text
        self.text_edit = QTextEdit()
        
        # Create main layout
        layout = QVBoxLayout()
        layout.addWidget(self.text_edit)
        
        # Create central widget and set layout
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # Open serial port (adjust parameters as needed)
        self.ser = serial.Serial('/dev/ttyUSB0', 9600)  # Change port and baud rate as needed

        # Start reading data from serial port
        self.read_serial()

    def read_serial(self):
        try:
            while True:
                # Read data from serial port
                data = self.ser.readline().decode().strip()  # Assuming text data, adjust decoding as needed

                # Append data to QTextEdit
                self.text_edit.append(data)
                
        except KeyboardInterrupt:
            self.ser.close()  # Close serial port when program is interrupted

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SerialReader()
    window.show()
    sys.exit(app.exec_())
