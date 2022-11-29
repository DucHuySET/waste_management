# This Python file uses the following encoding: utf-8
import sys
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QLine, QRect
from PyQt5.QtGui import QFont, QIcon
from ui.base_widget.utils_widget import *

class ExportScreenInfo (QMainWindow):
    def __init__(self, stackWidget, mainWindow, exportScreen):
        self.stackWidget = stackWidget
        self.mainWindow = mainWindow
        self.exportScreen = exportScreen
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

        self.divider01 = buildDivider()
        self.column01.addWidget(self.divider01)

        self.body = QHBoxLayout()
        # body.setStretch(1, 50)
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

        self.column_Input = QVBoxLayout()
        self.column_Input.setAlignment(Qt.AlignTop)
        self.column_Input.setSpacing(50)
        self.input_Field.setLayout(self.column_Input)
        
        self.declare = QLabel('Quy trình cân phế liệu xuất bán')
        self.declare.setObjectName('declare')
        self.declare.setFixedHeight(80)
        self.declare.setStyleSheet(f'''
        QLabel#declare {{
            background-color: transparent;
            border: none;
            border-radius: 0px;
            color: white;
        }}''')
        self.declare.setFont(QFont("Arial", 20))
        self.column_Input.addWidget(self.declare)

        self.row1 = QHBoxLayout()
        self.row1.addWidget(buildCardItem(700, 80, 'Lượt cân'))
        self.input1 = buildInputForm(500, 80)
        self.input1.input.setText("1")
        self.input1.input.textChanged.connect(self.setTurn)
        self.row1.addWidget(self.input1)
        self.column_Input.addLayout(self.row1)

        self.row2 = QHBoxLayout()
        self.row2.addWidget(buildCardItem(700, 80, 'Thùng bì'))
        self.input2 = buildInputForm(500, 80)
        self.input2.input.textChanged.connect(self.setPackage)
        self.row2.addWidget(self.input2)
        self.column_Input.addLayout(self.row2)
        
        self.row3 = QHBoxLayout()
        self.row3.addWidget(buildCardItem(700, 80, 'Chủng loại phế liệu'))
        self.input3 = buildInputForm(500, 80)
        self.input3.input.textChanged.connect(self.setType)
        self.row3.addWidget(self.input3)
        self.column_Input.addLayout(self.row3)

        self.row4 = QHBoxLayout()
        self.row4.addWidget(buildCardItem(700, 80, 'Xác nhận thông tin cân'))
        self.input4 = buildInputForm(500, 80)
        self.input4.input.textChanged.connect(self.setTurnInfo)
        self.row4.addWidget(self.input4)
        self.column_Input.addLayout(self.row4)

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

        self.turn = QLabel('Lượt cân: ')
        self.turn.setFixedHeight(100)
        self.turn.setStyleSheet(f'''
        QLabel {{
            background-color: #474747;
            border: none;
            border-radius: 10px;
            color: white;
        }}''')
        self.turn.setFont(QFont("Arial", 20))
        self.column_record.addWidget(self.turn)

        self.package = QLabel('Thùng bì: ')
        self.package.setFixedHeight(100)
        self.package.setStyleSheet(f'''
        QLabel {{
            background-color: #474747;
            border: none;
            border-radius: 10px;
            color: white;
        }}''')
        self.package.setFont(QFont("Arial", 20))
        self.column_record.addWidget(self.package)

        self.type = QLabel('Chủng loại phế liệu: ')
        self.type.setFixedHeight(100)
        self.type.setStyleSheet(f'''
        QLabel {{
            background-color: #474747;
            border: none;
            border-radius: 10px;
            color: white;
        }}''')
        self.type.setFont(QFont("Arial", 20))
        self.column_record.addWidget(self.type)

        self.measInfo = QLabel('Thông tin cân: ')
        self.measInfo.setFixedHeight(100)
        self.measInfo.setStyleSheet(f'''
        QLabel {{
            background-color: #474747;
            border: none;
            border-radius: 10px;
            color: white;
        }}''')
        self.measInfo.setFont(QFont("Arial", 20))
        self.column_record.addWidget(self.measInfo)

        self.rowAction = QHBoxLayout()
        self.rowAction.setSpacing(150)
        self.column_record.addLayout(self.rowAction)

        self.saveButton = buildButton("Lưu", 300, 80)
        self.saveButton.clicked.connect(self.turnSave)
        self.rowAction.addWidget(self.saveButton)

        self.cancelButton = buildButton("Hủy", 300, 80)
        self.cancelButton.clicked.connect(self.turnCancel)
        self.rowAction.addWidget(self.cancelButton)

        self.column_record.addWidget(sizedBox10())

        self.back_button = buildButton("Quay lại màn hình khai báo", 750, 80)
        self.back_button.clicked.connect(self.goToExportScr)
        self.column_record.addWidget(self.back_button)

        self.main_button = buildButton("Quay lại màn hình chính", 750, 80)
        self.main_button.clicked.connect(self.goToMainScr)
        self.column_record.addWidget(self.main_button)

        self.widget = QWidget()
        self.widget.setLayout(self.column01)
        self.setCentralWidget(self.widget)

        # self.setStaffName()
    def goToExportScr(self):
        self.stackWidget.setCurrentWidget(self.exportScreen)
    def goToMainScr(self):
        self.stackWidget.setCurrentWidget(self.mainWindow)
    def setTurn(self):
        self.turn.setText('Lượt cân: ' + self.input1.input.text())
    def setPackage(self):
        self.package.setText('Thùng bì: ' + self.input2.input.text())
    def setType(self):
        self.type.setText('Chủng loại phế liệu: ' + self.input3.input.text())
    def setTurnInfo(self):
        self.turn_info.setText('Thông tin lượt cân: ' + self.input4.input.text())
    def turnSave(self):
        self.currentTurn = self.input1.input.text()
        self.clearField()
        self.input1.input.setText(str(int(self.currentTurn)+1))
        self.input1.input.setFocus()
        print("saved")
    def turnCancel(self):
        self.currentTurn = self.input1.input.text()
        self.clearField()
        self.input1.input.setText(self.currentTurn)
        self.input1.input.setFocus()
        print("canceled")
    def clearField(self):
        self.input1.input.clear()
        self.input2.input.clear()
        self.input3.input.clear()
        self.input4.input.clear()

