# This Python file uses the following encoding: utf-8
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QLine, QRect, QEvent
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
        self.setObjectName('divider')
        self.setText('')
        self.setStyleSheet(f'''
        QWidget#divider {{
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
        column.setAlignment(Qt.AlignLeft)
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
        self.column = QVBoxLayout()
        self.column.setAlignment(Qt.AlignVCenter)

        self.input = QLineEdit()
        self.input.setFont(QFont('Arial', 20))
        self.column.addWidget(self.input)

        self.setLayout(self.column)
    def event(self, event):
        if event.type() == QEvent.KeyPress:
            if event.key() in (Qt.Key_Return, Qt.Key_Enter):
                self.focusNextPrevChild(True)
        return super().event(event)


