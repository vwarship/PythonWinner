import sys
from PyQt5.QtWidgets import QMessageBox, QApplication, QWidget, QVBoxLayout, QTextEdit, QPushButton


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hello")

        self.edit_hello = QTextEdit("Hello World!")
        self.btn_press = QPushButton("Press me")

        self.btn_press.clicked.connect(self.btn_press_clicked)

        layout = QVBoxLayout()
        layout.addWidget(self.edit_hello)
        layout.addWidget(self.btn_press)
        self.setLayout(layout)

    def btn_press_clicked(self):
        QMessageBox.information(self, "HI", "Press me!")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    app.exec_()
