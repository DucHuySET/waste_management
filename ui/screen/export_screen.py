# This Python file uses the following encoding: utf-8
import sys
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QLine, QRect
from PyQt5.QtGui import QFont, QIcon
from ui.base_widget.utils_widget import *

class ExportScreen (QMainWindow):
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
        column01.setAlignment(Qt.AlignTop)

        turn_info = QLabel('Thông tin lượt cân đầu ra')
        turn_info.setFont(QFont("Arial", 20))
        column01.addWidget(turn_info)

        divider01 = buildDivider()
        column01.addWidget(divider01)

        body = QHBoxLayout()
        # body.setStretch(1, 50)
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


        # inputField = buildCardBase(500,900)
        # body.addWidget(inputField)

        # recordField = buildCardBase(750,900)
        # body.addWidget(recordField)

        column_Input = QVBoxLayout()
        column_Input.setAlignment(Qt.AlignTop)
        input_Field.setLayout(column_Input)

        row1 = QHBoxLayout()
        row1.setContentsMargins(0,0,0,0)
        # row1.setAlignment(Qt.AlignLeft)
        row1.addWidget(buildCardItem(700, 100, 'Lần cân'))
        row1.addWidget(buildInputForm(500, 70))
        column_Input.addLayout(row1)

        row2 = QHBoxLayout()
        row2.setContentsMargins(0,0,0,0)
        # row1.setAlignment(Qt.AlignLeft)
        row2.addWidget(buildCardItem(700, 100, 'Thùng bì'))
        row2.addWidget(buildInputForm(500, 70))
        column_Input.addLayout(row2)
        
        row3 = QHBoxLayout()
        row3.setContentsMargins(0,0,0,0)
        # row1.setAlignment(Qt.AlignLeft)
        row3.addWidget(buildCardItem(700, 100, 'Chủng loại phế liệu'))
        row3.addWidget(buildInputForm(500, 70))
        column_Input.addLayout(row3)

        row4 = QHBoxLayout()
        row4.setContentsMargins(0,0,0,0)
        # row1.setAlignment(Qt.AlignLeft)
        row4.addWidget(buildCardItem(700, 100, 'Nhân viên cân'))
        row4.addWidget(buildInputForm(500, 70))
        column_Input.addLayout(row4)

        row5 = QHBoxLayout()
        row5.setContentsMargins(0,0,0,0)
        # row1.setAlignment(Qt.AlignLeft)
        row5.addWidget(buildCardItem(700, 100, 'Nhân viên cân'))
        row5.addWidget(buildInputForm(500, 70))
        column_Input.addLayout(row5)

        column_record = QVBoxLayout()
        recordField.setLayout(column_record)

        back_button = QPushButton()
        back_button.setText('Quay lại')
        # back_button.clicked.connect(lambda: )
        column_record.addWidget(back_button)

        widget = QWidget()
        widget.setLayout(column01)
        self.setCentralWidget(widget)
        