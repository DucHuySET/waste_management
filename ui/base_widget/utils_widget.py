# This Python file uses the following encoding: utf-8
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QLine, QRect
from PyQt5.QtGui import QFont, QIcon

class buildCardBase(QWidget):
    def __init__(self,width, height):
        super().__init__()
        self.setFixedSize(width, height)
        self.setStyleSheet(f'''
        QWidget {{
            background-color: black;
            border: 2px solid #3399ff;
            border-radius: 20px
        }}''')

        self.uiComponents()
    def uiComponents(self):
        column01 = QVBoxLayout()

        self.setLayout(column01)

class buildDivider(QLabel):
    def __init__(self):
        super().__init__()
        self.setFixedHeight(2)
        self.setText('')
        self.setStyleSheet(f'''
        QWidget {{
            background-color: white;
            border: 2px solid #3399ff;
        }}''')

class buildCardItem(QWidget):
    width = 0
    height = 0
    text = ''
    def __init__(self,width, height, text):
        super().__init__()
        self.text = text
        self.width = width
        self.height = height
        self.setFixedSize(width, height)
        self.setStyleSheet(f'''
        QWidget {{
            background-color: white;
            border: 2px solid #3399ff;
            border-radius: 10px
        }}''')
        self.components()
    
    def components(self):
        column = QVBoxLayout()
        column.setAlignment(Qt.AlignCenter)

        label = QLabel(self.text)
        label.setFont(QFont('Arial', 20))
        column.addWidget(label)
        self.setLayout(column)
        self.setFixedSize(self.width, self.height)

class buildInputForm(QWidget):
    def __init__(self, width, height):
        super().__init__()
        self.setFixedSize(width, height)
        self.setStyleSheet(f'''
        QWidget {{
            background-color: white;
            border: 2px solid #3399ff;
            border-radius: 10px
        }}''')
        self.components()
    def components(self):
        column = QVBoxLayout()
        column.setAlignment(Qt.AlignVCenter)

        input = QTextEdit()
        input.setFont(QFont('Arial', 15))
        column.addWidget(input)

        self.setLayout(column)

