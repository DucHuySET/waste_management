# This Python file uses the following encoding: utf-8
import sys
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QLine, QRect
from PyQt5.QtGui import QFont, QIcon
from ui.base_widget.utils_widget import *

class Import_screen(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Waste Management")
        self.setGeometry(0,0,1920,1080)
        self.setStyleSheet("background-color: white")
        self.uiComponents()
        self.show()
    def uiComponents(self):
        column01 = QVBoxLayout()
        column01.setContentsMargins(20,20,20,20)

        turn_info = QLabel('Thông tin lượt cân đầu vào')
        turn_info.setFont(QFont("Arial", 20))
        column01.addWidget(turn_info)

        divider01 = QLabel('')
        divider01.setFixedHeight(2)
        divider01.setStyleSheet(f'''
        QLabel {{
            background-color: white;
            border-radius: 20px;
            border: 2px solid black;
        }}''')
        column01.addWidget(divider01)

        body = QHBoxLayout()
        column01.addLayout(body)

        input_Field = QWidget()
        input_Field.setObjectName("input_Field")
        input_Field.setFixedSize(1100,900)
        input_Field.setStyleSheet(f'''
        QWidget {{
            background-color: white;
            border: 2px solid #3399ff;
            border-radius: 20px
        }}''')
        body.addWidget(input_Field)

        recordField = QWidget()
        recordField.setObjectName("recordField")
        recordField.setStyleSheet(f'''
        QWidget {{
            background-color: white;
            border: 2px solid #3399ff;
            border-radius: 20px
        }}''')
        body.addWidget(recordField)

        listInput = QVBoxLayout()
        input_Field.setLayout(listInput)

        widget = QWidget()
        widget.setLayout(column01)
        self.setCentralWidget(widget)