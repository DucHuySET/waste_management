# This Python file uses the following encoding: utf-8
import sys
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QLine, QRect
from PyQt5.QtGui import QFont, QIcon
from ui.base_widget.utils_widget import *

class ExportScreen (QMainWindow):
    def __init__(self, stackWidget, mainWindow):
        self.stackWidget = stackWidget
        self.mainWindow = mainWindow
        # self.exportScreenInfo = exportScreenInfo
        super().__init__()
        self.setWindowTitle("Waste Management")
        self.setGeometry(0,0,1920,1080)
        self.setStyleSheet("background-color: #1d212d")
        self.uiComponents()
        self.show()
    def uiComponents(self):
        self.column01 = QVBoxLayout()
        self.column01.setContentsMargins(20,20,20,20)
        self.column01.setAlignment(Qt.AlignTop)

        self.turn_info = QLabel('Thông tin lượt cân đầu ra')
        self.turn_info.setFont(QFont("Arial", 20))
        self.turn_info.setStyleSheet("color: white")
        self.column01.addWidget(self.turn_info)

        # self.divider01 = buildDivider()
        # self.column01.addWidget(self.divider01)

        self.body = QHBoxLayout()
        self.column01.addLayout(self.body)

        self.input_Field = QWidget()
        self.input_Field.setObjectName("input_Field")
        self.input_Field.setFixedSize(1100,900)
        self.input_Field.setStyleSheet(f'''
        QWidget {{
            background-color: #2e2e2e;
            border: none;
            border-radius: 20px
        }}''')
        self.body.addWidget(self.input_Field)

        self.recordField = QWidget()
        self.recordField.setObjectName("recordField")
        self.recordField.setStyleSheet(f'''
        QWidget {{
            background-color: #2e2e2e;
            border: none;
            border-radius: 20px
        }}''')
        self.body.addWidget(self.recordField)


        # inputField = buildCardBase(500,900)
        # body.addWidget(inputField)

        # recordField = buildCardBase(750,900)
        # body.addWidget(recordField)

        self.column_Input = QVBoxLayout()
        self.column_Input.setAlignment(Qt.AlignTop)
        self.column_Input.setSpacing(50)
        self.input_Field.setLayout(self.column_Input)
        
        self.declare = QLabel('Quy trình khai báo thu gom phế liệu')
        self.declare.setObjectName('declare')
        self.declare.setFixedHeight(80)
        self.declare.setStyleSheet(
            "background-color: transparent;"
            "border: none;"
            "border-radius: 0px;"
            "color: white;"
        )
        self.declare.setFont(QFont("Arial", 20))
        self.column_Input.addWidget(self.declare)

        self.row1 = QHBoxLayout()
        self.row1.addWidget(buildCardItem(700, 80, 'Nhân viên phụ trách cân đầu vào'))
        self.input1 = buildInputForm(500, 80)
        self.input1.input.textChanged.connect(self.setStaffName)
        self.row1.addWidget(self.input1)
        self.column_Input.addLayout(self.row1)

        self.row2 = QHBoxLayout()
        self.row2.setContentsMargins(0,0,0,0)
        self.row2.addWidget(buildCardItem(700, 80, 'Công ty thu gom phế liệu'))
        self.input2 = buildInputForm(500, 80)
        self.input2.input.textChanged.connect(self.setCompName)
        self.row2.addWidget(self.input2)
        self.column_Input.addLayout(self.row2)
        
        self.row3 = QHBoxLayout()
        self.row3.setContentsMargins(0,0,0,0)
        self.row3.addWidget(buildCardItem(700, 80, 'Xe vận tải'))
        self.input3 = buildInputForm(500, 80)
        self.input3.input.textChanged.connect(self.setCarLabel)
        self.row3.addWidget(self.input3)
        self.column_Input.addLayout(self.row3)

        self.rowConfirm = QHBoxLayout()
        self.rowConfirm.setAlignment(Qt.AlignHCenter)
        self.column_Input.addLayout(self.rowConfirm)
        self.confirmButton = buildButton("Xác nhận thông tin", 500, 60)
        self.rowConfirm.addWidget(self.confirmButton)

        self.column_record = QVBoxLayout()
        self.column_record.setAlignment(Qt.AlignTop)
        self.recordField.setLayout(self.column_record)

        self.recordLabel = QLabel('Thông tin bản ghi')
        self.recordLabel.setFixedHeight(100)
        self.recordLabel.setStyleSheet(f'''
        QLabel {{
            background-color: transparent;
            border: none;
            border-radius: 0px;
            color: white;
        }}''')
        self.recordLabel.setFont(QFont("Arial", 20))
        self.column_record.addWidget(self.recordLabel)

        self.staffName = QLabel('Tên nhân viên: ')
        self.staffName.setFixedHeight(100)
        self.staffName.setStyleSheet(f'''
        QLabel {{
            background-color: #474747;
            border: none;
            border-radius: 10px;
            color: white;
        }}''')
        self.staffName.setFont(QFont("Arial", 20))
        self.column_record.addWidget(self.staffName)

        self.compName = QLabel('Tên công ty: ')
        self.compName.setFixedHeight(100)
        self.compName.setStyleSheet(f'''
        QLabel {{
            background-color: #474747;
            border: none;
            border-radius: 10px;
            color: white;
        }}''')
        self.compName.setFont(QFont("Arial", 20))
        self.column_record.addWidget(self.compName)

        self.carLabel = QLabel('Biển kiểm soát: ')
        self.carLabel.setFixedHeight(100)
        self.carLabel.setStyleSheet(f'''
        QLabel {{
            background-color: #474747;
            border: none;
            border-radius: 10px;
            color: white;
        }}''')
        self.carLabel.setFont(QFont("Arial", 20))
        self.column_record.addWidget(self.carLabel)

        self.back_button = buildButton("Quay lại", 750,80)
        self.back_button.clicked.connect(self.goToMainScr)
        self.column_record.addWidget(self.back_button)

        self.next_button = buildButton("Thông tin lượt cân", 750, 80)
        # self.next_button.clicked.connect(self.goToInfoScr)
        self.column_record.addWidget(self.next_button)

        self.widget = QWidget()
        self.widget.setLayout(self.column01)
        self.setCentralWidget(self.widget)

        # self.setStaffName()
    def goToMainScr(self):
        self.stackWidget.setCurrentWidget(self.mainWindow)
    # def goToInfoScr(self):
    #     self.stackWidget.setCurrentWidget(self.exportScreenInfo)
    def setStaffName(self):
        self.staffName.setText('Thông tin nhân viên: ' + self.input1.input.text())
    def setCompName(self):
        self.compName.setText('Tên công ty: ' + self.input2.input.text())
    def setCarLabel(self):
        self.carLabel.setText('Biển kiểm soát: ' + self.input3.input.text())

