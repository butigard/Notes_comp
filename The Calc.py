import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.equation = ""
        self.par = "1"

        # Layout
        self.grid = QGridLayout()
        self.setLayout(self.grid)
        self.setGeometry(10, 10, 300, 300)

        # Widgets
        self.display = QLabel("")
        self.grid.addWidget(self.display, 1, 1, 1, 3)

        self.button1 = QPushButton("1")
        self.grid.addWidget(self.button1, 5, 1, 1, 1)

        self.button2 = QPushButton("2")
        self.grid.addWidget(self.button2, 5, 2, 1, 1)

        self.button3 = QPushButton("3")
        self.grid.addWidget(self.button3, 5, 3, 1, 1)

        self.button4 = QPushButton("4")
        self.grid.addWidget(self.button4, 4, 1, 1, 1)

        self.button5 = QPushButton("5")
        self.grid.addWidget(self.button5, 4, 2, 1, 1)

        self.button6 = QPushButton("6")
        self.grid.addWidget(self.button6, 4, 3, 1, 1)

        self.button7 = QPushButton("7")
        self.grid.addWidget(self.button7, 3, 1, 1, 1)

        self.button8 = QPushButton("8")
        self.grid.addWidget(self.button8, 3, 2, 1, 1)

        self.button9 = QPushButton("9")
        self.grid.addWidget(self.button9, 3, 3, 1, 1)

        self.button0 = QPushButton("0")
        self.grid.addWidget(self.button0, 6, 1, 1, 2)

        self.button_dot = QPushButton(".")
        self.grid.addWidget(self.button_dot, 6, 3, 1, 1)

        self.button_add = QPushButton("+")
        self.grid.addWidget(self.button_add, 5, 4, 1, 1)

        self.button_subtract = QPushButton("-")
        self.grid.addWidget(self.button_subtract, 4, 4, 1, 1)

        self.button_multiply = QPushButton("*")
        self.grid.addWidget(self.button_multiply, 3, 4, 1, 1)

        self.button_divide = QPushButton("/")
        self.grid.addWidget(self.button_divide, 2, 4, 1, 1)

        self.button_equal = QPushButton("=")
        self.grid.addWidget(self.button_equal, 6, 4, 1, 1)

        self.button_clear = QPushButton("Clear")
        self.grid.addWidget(self.button_clear, 2, 1, 1, 1)

        self.button_exponent = QPushButton("^x")
        self.grid.addWidget(self.button_exponent, 2, 3, 1, 1)

        self.button_square = QPushButton("^2")
        self.grid.addWidget(self.button_square, 2, 2, 1, 1)

        # Signals/Slots
        self.button1.clicked.connect(lambda: self.concat("1"))
        self.button2.clicked.connect(lambda: self.concat("2"))
        self.button3.clicked.connect(lambda: self.concat("3"))
        self.button4.clicked.connect(lambda: self.concat("4"))
        self.button5.clicked.connect(lambda: self.concat("5"))
        self.button6.clicked.connect(lambda: self.concat("6"))
        self.button7.clicked.connect(lambda: self.concat("7"))
        self.button8.clicked.connect(lambda: self.concat("8"))
        self.button9.clicked.connect(lambda: self.concat("9"))
        self.button0.clicked.connect(lambda: self.concat("0"))
        self.button_dot.clicked.connect(lambda: self.concat("."))
        self.button_add.clicked.connect(lambda: self.concat("+"))
        self.button_multiply.clicked.connect(lambda: self.concat("*"))
        self.button_subtract.clicked.connect(lambda: self.concat("-"))
        self.button_divide.clicked.connect(lambda: self.concat("/"))
        self.button_equal.clicked.connect(self.equal)
        self.button_clear.clicked.connect(self.clear)
        self.button_exponent.clicked.connect(lambda: self.concat("**"))
        self.button_square.clicked.connect(lambda: self.concat("**2"))



        # Set Style
        self.set_style()

        # Draw
        self.show()

    def set_style(self):
        style_sheet = "The_Calc.css"
        with open(style_sheet) as f:
            self.setStyleSheet(f.read())
    def concat(self, val):
        self.equation += val
        self.display.setText(self.equation)
    def equal(self):
        try:
            self.equation = str(eval(self.equation))
            self.display.setText(str(self.equation))
        except:
            self.display.setText("ERROR")
    def clear(self):
        self.equation = ""
        self.display.setText(str(self.equation))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    gui = Window()
    sys.exit(app.exec())