# This Python file uses the following encoding: utf-8
import sys
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QLine, QRect, pyqtSlot, pyqtSignal
from PyQt5.QtGui import QFont, QIcon

# from ui.screen.import_screen import *
# from ui.screen.export_screen import *
from ui.base_widget.utils_widget import *

# from pathlib import Path

# from PySide2.QtGui import QGuiApplication
# from PySide2.QtQml import QQmlApplicationEngine
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Waste Management")
        self.setGeometry(0,0,1920,1080)
        self.setStyleSheet("background-color: #dae4f0")
        self.uiComponents()
        self.show()

    def uiComponents(self):
        #creating Column
        column = QVBoxLayout()
        column.setAlignment(Qt.AlignCenter)
        column.setSpacing(100)

        label = QLabel("Quản lý nhập, xuất kho phế liệu")
        label.setAlignment(Qt.AlignCenter)
        label.setFont(QFont('Arial', 30, 1))
        column.addWidget(label)

        row = QHBoxLayout()
        row.setAlignment(Qt.AlignCenter)
        row.setSpacing(50)
        column.addLayout(row)

        button_importScr = QPushButton("Quản lý lượt cân \nđầu vào")
        button_importScr.setFixedHeight(200)
        button_importScr.setFixedWidth(300)
        button_importScr.setFont(QFont("Arial", 20))
        button_importScr.setStyleSheet(f'''
        QPushButton {{
            color: black;
            background-color: white;
            padding: 12px;
            border-radius: 20px;
        }}''')
        button_importScr.clicked.connect(self.goToImportScr)
        row.addWidget(button_importScr)

        button_exportScr = QPushButton("Quản lý lượt cân \nđầu ra")
        button_exportScr.setFixedHeight(200)
        button_exportScr.setFixedWidth(300)
        button_exportScr.setFont(QFont("Arial", 20))
        button_exportScr.setStyleSheet(f'''
        QPushButton {{
            color: black;
            background-color: white;
            padding: 12px;
            border-radius: 20px;
        }}''')
        button_exportScr.clicked.connect(self.goToExportScr)
        row.addWidget(button_exportScr)

        # # creating label
        # label = QLabel("Quản lý nhập, xuất kho phế liệu", self)
  
        # # setting geometry to label
        # label.set
  
        # # adding border to label
        # label.setStyleSheet("border : 2px solid black")
        widget = QWidget()
        widget.setLayout(column)
        self.setCentralWidget(widget)
        # # opening window in maximized size
        self.showMaximized()
    def goToImportScr(self):
        widget_stack.setCurrentWidget(import_screen)
    def goToExportScr(self):
        widget_stack.setCurrentWidget(export_screen)

class Import_screen(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Waste Management")
        self.setGeometry(0,0,1920,1080)
        self.setStyleSheet("background-color: white")
        self.uiComponents()
        self.show()
    def uiComponents(self):
        self.column01 = QVBoxLayout()
        self.column01.setContentsMargins(20,20,20,20)

        self.turn_info = QLabel('Thông tin lượt cân đầu vào')
        self.turn_info.setFont(QFont("Arial", 20))
        self.column01.addWidget(self.turn_info)

        self.divider01 = QLabel('')
        self.divider01.setObjectName('divider01')
        self.divider01.setFixedHeight(2)
        self.divider01.setStyleSheet(f'''
        divider01 {{
            background-color: white;
            border-radius: 20px;
            border: 2px solid black;
        }}''')
        self.column01.addWidget(self.divider01)

        self.body = QHBoxLayout()
        self.column01.addLayout(self.body)

        self.input_Field = QWidget()
        self.input_Field.setObjectName("input_Field")
        self.input_Field.setFixedSize(1100,900)
        self.input_Field.setStyleSheet(f'''
        QWidget {{
            background-color: white;
            border: 2px solid #3399ff;
            border-radius: 20px
        }}''')
        self.body.addWidget(self.input_Field)

        self.recordField = QWidget()
        self.recordField.setObjectName("recordField")
        self.recordField.setStyleSheet(f'''
        QWidget {{
            background-color: white;
            border: 2px solid #3399ff;
            border-radius: 20px
        }}''')
        self.body.addWidget(self.recordField)

        self.column_Input = QVBoxLayout()
        self.column_Input.setAlignment(Qt.AlignTop)
        self.column_Input.setSpacing(50)
        self.input_Field.setLayout(self.column_Input)
        
        self.declare = QLabel('Quy trình nhập phế liệu đầu vào')
        self.declare.setObjectName('declare')
        self.declare.setFixedHeight(80)
        self.declare.setStyleSheet(f'''
        QLabel {{
            background-color: white;
            border: none;
            border-radius: 0px
        }}''')
        self.declare.setFont(QFont("Arial", 20))
        self.column_Input.addWidget(self.declare)

        # self.inputDivider = buildDivider()
        # self.column_Input.addWidget(self.inputDivider)

        self.row1 = QHBoxLayout()
        self.row1.addWidget(buildCardItem(700, 80, 'Nhân viên phụ trách cân đầu vào'))
        self.input1 = buildInputForm(500, 80)
        self.input1.input.textChanged.connect(self.setStaffNameMeas)
        self.row1.addWidget(self.input1)
        self.column_Input.addLayout(self.row1)

        self.row2 = QHBoxLayout()
        self.row2.setContentsMargins(0,0,0,0)
        self.row2.addWidget(buildCardItem(700, 80, 'Nhân viên tập kết phế liệu'))
        self.input2 = buildInputForm(500, 80)
        self.input2.input.textChanged.connect(self.setStaffNameColl)
        self.row2.addWidget(self.input2)
        self.column_Input.addLayout(self.row2)
        
        self.row3 = QHBoxLayout()
        self.row3.setContentsMargins(0,0,0,0)
        self.row3.addWidget(buildCardItem(700, 80, 'Thùng bì'))
        self.input3 = buildInputForm(500, 80)
        self.input3.input.textChanged.connect(self.setPackage)
        self.row3.addWidget(self.input3)
        self.column_Input.addLayout(self.row3)

        self.row4 = QHBoxLayout()
        self.row4.setContentsMargins(0,0,0,0)
        self.row4.addWidget(buildCardItem(700, 80, 'Chủng loại phế liệu'))
        self.input4 = buildInputForm(500, 80)
        self.input4.input.textChanged.connect(self.setType)
        self.row4.addWidget(self.input4)
        self.column_Input.addLayout(self.row4)

        self.row5 = QHBoxLayout()
        self.row5.setContentsMargins(0,0,0,0)
        self.row5.addWidget(buildCardItem(700, 80, 'Xác nhận khối lượng cân'))
        self.input5 = buildInputForm(500, 80)
        self.input5.input.textChanged.connect(self.setInfo)
        self.row5.addWidget(self.input5)
        self.column_Input.addLayout(self.row5)

        self.confirm = QLabel('Xác nhận thông tin')
        self.confirm.setFont(QFont("Arial", 20))
        self.column_Input.addWidget(self.confirm)

        self.column_record = QVBoxLayout()
        self.column_record.setAlignment(Qt.AlignTop)
        self.recordField.setLayout(self.column_record)

        self.recordLabel = QLabel('Thông tin bản ghi')
        self.recordLabel.setFixedHeight(100)
        self.recordLabel.setStyleSheet(f'''
        QLabel {{
            background-color: white;
            border: none;
            border-radius: 0px
        }}''')
        self.recordLabel.setFont(QFont("Arial", 20))
        self.column_record.addWidget(self.recordLabel)

        self.recordDivider = buildDivider()
        self.column_record.addWidget(self.recordDivider)

        self.staffNameMeas = QLabel('Tên nhân viên cân: ')
        self.staffNameMeas.setFixedHeight(100)
        self.staffNameMeas.setStyleSheet(f'''
        QLabel {{
            background-color: white;
            border: none;
            border-radius: 0px
        }}''')
        self.staffNameMeas.setFont(QFont("Arial", 20))
        self.column_record.addWidget(self.staffNameMeas)

        self.staffNameColl = QLabel('Nhân viên tập kết phế liệu: ')
        self.staffNameColl.setFixedHeight(100)
        self.staffNameColl.setStyleSheet(f'''
        QLabel {{
            background-color: white;
            border: none;
            border-radius: 0px
        }}''')
        self.staffNameColl.setFont(QFont("Arial", 20))
        self.column_record.addWidget(self.staffNameColl)

        self.package = QLabel('Thùng bì ')
        self.package.setFixedHeight(100)
        self.package.setStyleSheet(f'''
        QLabel {{
            background-color: white;
            border: none;
            border-radius: 0px
        }}''')
        self.package.setFont(QFont("Arial", 20))
        self.column_record.addWidget(self.package)

        self.type = QLabel('Chủng loại phế liệu: ')
        self.type.setFixedHeight(100)
        self.type.setStyleSheet(f'''
        QLabel {{
            background-color: white;
            border: none;
            border-radius: 0px
        }}''')
        self.type.setFont(QFont("Arial", 20))
        self.column_record.addWidget(self.type)

        self.measInfo = QLabel('Thông tin cân: ')
        self.measInfo.setFixedHeight(100)
        self.measInfo.setStyleSheet(f'''
        QLabel {{
            background-color: white;
            border: none;
            border-radius: 0px
        }}''')
        self.measInfo.setFont(QFont("Arial", 20))
        self.column_record.addWidget(self.measInfo)

        self.back_button = QPushButton()
        self.back_button.setFixedHeight(80)
        self.back_button.setText('Quay lại')
        self.back_button.clicked.connect(self.goToMainScr)
        self.column_record.addWidget(self.back_button)

        self.widget = QWidget()
        self.widget.setLayout(self.column01)
        self.setCentralWidget(self.widget)

        # self.setStaffName()
    def goToMainScr(self):
        widget_stack.setCurrentWidget(mainWindow)
    def setStaffNameMeas(self):
        self.staffNameMeas.setText('Thông tin nhân viên cân: ' + self.input1.input.text())
    def setStaffNameColl(self):
        self.staffNameColl.setText('Thông tin nhân viên tập kết: ' + self.input2.input.text())
    def setPackage(self):
        self.package.setText('Thùng bì: ' + self.input3.input.text())
    def setType(self):
        self.type.setText('Chủng loại phế liệu: ' + self.input4.input.text())
    def setInfo(self):
        self.measInfo.setText('Khối lượng cân: ' + self.input5.input.text())


        widget = QWidget()
        widget.setLayout(self.column01)
        self.setCentralWidget(widget)

class ExportScreen (QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Waste Management")
        self.setGeometry(0,0,1920,1080)
        self.setStyleSheet("background-color: white")
        self.uiComponents()
        self.show()
    def uiComponents(self):
        self.column01 = QVBoxLayout()
        self.column01.setContentsMargins(20,20,20,20)
        self.column01.setAlignment(Qt.AlignTop)

        self.turn_info = QLabel('Thông tin lượt cân đầu ra')
        self.turn_info.setFont(QFont("Arial", 20))
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
            background-color: #eaebe8;
            border: 2px solid #3399ff;
            border-radius: 20px
        }}''')
        self.body.addWidget(self.input_Field)

        self.recordField = QWidget()
        self.recordField.setObjectName("recordField")
        self.recordField.setStyleSheet(f'''
        QWidget {{
            background-color: #eaebe8;
            border: 2px solid #3399ff;
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
        self.declare.setStyleSheet(f'''
        QLabel {{
            background-color: white;
            border: none;
            border-radius: 0px
        }}''')
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

        self.confirm = QLabel('Xác nhận thông tin')
        self.confirm.setFont(QFont("Arial", 20))
        self.column_Input.addWidget(self.confirm)

        self.column_record = QVBoxLayout()
        self.column_record.setAlignment(Qt.AlignTop)
        self.recordField.setLayout(self.column_record)

        self.recordLabel = QLabel('Thông tin bản ghi')
        self.recordLabel.setFixedHeight(100)
        self.recordLabel.setStyleSheet(f'''
        QLabel {{
            background-color: white;
            border: none;
            border-radius: 0px
        }}''')
        self.recordLabel.setFont(QFont("Arial", 20))
        self.column_record.addWidget(self.recordLabel)

        self.staffName = QLabel('Tên nhân viên: ')
        self.staffName.setFixedHeight(100)
        self.staffName.setStyleSheet(f'''
        QLabel {{
            background-color: white;
            border: none;
            border-radius: 0px
        }}''')
        self.staffName.setFont(QFont("Arial", 20))
        self.column_record.addWidget(self.staffName)

        self.compName = QLabel('Tên công ty: ')
        self.compName.setFixedHeight(100)
        self.compName.setStyleSheet(f'''
        QLabel {{
            background-color: white;
            border: none;
            border-radius: 0px
        }}''')
        self.compName.setFont(QFont("Arial", 20))
        self.column_record.addWidget(self.compName)

        self.carLabel = QLabel('Biển kiểm soát: ')
        self.carLabel.setFixedHeight(100)
        self.carLabel.setStyleSheet(f'''
        QLabel {{
            background-color: white;
            border: none;
            border-radius: 0px
        }}''')
        self.carLabel.setFont(QFont("Arial", 20))
        self.column_record.addWidget(self.carLabel)

        self.back_button = QPushButton()
        self.back_button.setFixedHeight(80)
        self.back_button.setText('Quay lại')
        self.back_button.clicked.connect(self.goToMainScr)
        self.column_record.addWidget(self.back_button)

        self.next_button = QPushButton()
        self.next_button.setFixedHeight(80)
        self.next_button.setText('Thông tin lượt cân')
        self.next_button.clicked.connect(self.goToInfoScr)
        self.column_record.addWidget(self.next_button)

        self.widget = QWidget()
        self.widget.setLayout(self.column01)
        self.setCentralWidget(self.widget)

        # self.setStaffName()
    def goToMainScr(self):
        widget_stack.setCurrentWidget(mainWindow)
    def goToInfoScr(self):
        widget_stack.setCurrentWidget(export_screen_info)
    def setStaffName(self):
        self.staffName.setText('Thông tin nhân viên: ' + self.input1.input.text())
    def setCompName(self):
        self.compName.setText('Tên công ty: ' + self.input2.input.text())
    def setCarLabel(self):
        self.carLabel.setText('Biển kiểm soát: ' + self.input3.input.text())

class ExportScreenInfo (QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Waste Management")
        self.setGeometry(0,0,1920,1080)
        self.setStyleSheet("background-color: white")
        self.uiComponents()
        self.show()
    def uiComponents(self):
        self.column01 = QVBoxLayout()
        self.column01.setContentsMargins(20,20,20,20)
        self.column01.setAlignment(Qt.AlignTop)

        self.turn_info = QLabel('Thông tin lượt cân đầu ra')
        self.turn_info.setFont(QFont("Arial", 20))
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
            background-color: #eaebe8;
            border: 2px solid #3399ff;
            border-radius: 20px
        }}''')
        self.body.addWidget(self.input_Field)

        self.recordField = QWidget()
        self.recordField.setObjectName("recordField")
        self.recordField.setStyleSheet(f'''
        QWidget {{
            background-color: #eaebe8;
            border: 2px solid #3399ff;
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
        QLabel {{
            background-color: white;
            border: none;
            border-radius: 0px
        }}''')
        self.declare.setFont(QFont("Arial", 20))
        self.column_Input.addWidget(self.declare)

        self.row1 = QHBoxLayout()
        self.row1.addWidget(buildCardItem(700, 80, 'Lượt cân'))
        self.input1 = buildInputForm(500, 80)
        self.input1.input.textChanged.connect(self.setStaffName)
        self.row1.addWidget(self.input1)
        self.column_Input.addLayout(self.row1)

        self.row2 = QHBoxLayout()
        self.row2.setContentsMargins(0,0,0,0)
        self.row2.addWidget(buildCardItem(700, 80, 'Thùng bì'))
        self.input2 = buildInputForm(500, 80)
        self.input2.input.textChanged.connect(self.setCompName)
        self.row2.addWidget(self.input2)
        self.column_Input.addLayout(self.row2)
        
        self.row3 = QHBoxLayout()
        self.row3.setContentsMargins(0,0,0,0)
        self.row3.addWidget(buildCardItem(700, 80, 'Chủng loại phế liệu'))
        self.input3 = buildInputForm(500, 80)
        self.input3.input.textChanged.connect(self.setCarLabel)
        self.row3.addWidget(self.input3)
        self.column_Input.addLayout(self.row3)

        self.row4 = QHBoxLayout()
        self.row4.setContentsMargins(0,0,0,0)
        self.row4.addWidget(buildCardItem(700, 80, 'Xác nhận thông tin cân'))
        self.input4 = buildInputForm(500, 80)
        self.input4.input.textChanged.connect(self.setCarLabel)
        self.row4.addWidget(self.input4)
        self.column_Input.addLayout(self.row4)

        self.confirm = QLabel('Xác nhận thông tin')
        self.confirm.setFont(QFont("Arial", 20))
        self.column_Input.addWidget(self.confirm)

        self.column_record = QVBoxLayout()
        self.column_record.setAlignment(Qt.AlignTop)
        self.recordField.setLayout(self.column_record)

        self.recordLabel = QLabel('Thông tin bản ghi')
        self.recordLabel.setFixedHeight(100)
        self.recordLabel.setStyleSheet(f'''
        QLabel {{
            background-color: white;
            border: none;
            border-radius: 0px
        }}''')
        self.recordLabel.setFont(QFont("Arial", 20))
        self.column_record.addWidget(self.recordLabel)

        self.turn = QLabel('Lượt cân: ')
        self.turn.setFixedHeight(100)
        self.turn.setStyleSheet(f'''
        QLabel {{
            background-color: white;
            border: none;
            border-radius: 0px
        }}''')
        self.turn.setFont(QFont("Arial", 20))
        self.column_record.addWidget(self.turn)

        self.package = QLabel('Thùng bì: ')
        self.package.setFixedHeight(100)
        self.package.setStyleSheet(f'''
        QLabel {{
            background-color: white;
            border: none;
            border-radius: 0px
        }}''')
        self.package.setFont(QFont("Arial", 20))
        self.column_record.addWidget(self.package)

        self.type = QLabel('Chủng loại phế liệu: ')
        self.type.setFixedHeight(100)
        self.type.setStyleSheet(f'''
        QLabel {{
            background-color: white;
            border: none;
            border-radius: 0px
        }}''')
        self.type.setFont(QFont("Arial", 20))
        self.column_record.addWidget(self.type)

        self.measInfo = QLabel('Thông tin cân: ')
        self.measInfo.setFixedHeight(100)
        self.measInfo.setStyleSheet(f'''
        QLabel {{
            background-color: white;
            border: none;
            border-radius: 0px
        }}''')
        self.measInfo.setFont(QFont("Arial", 20))
        self.column_record.addWidget(self.measInfo)

        self.back_button = QPushButton()
        self.back_button.setFixedHeight(80)
        self.back_button.setText('Quay lại màn hình khai báo')
        self.back_button.clicked.connect(self.goToExportScr)
        self.column_record.addWidget(self.back_button)

        self.main_button = QPushButton()
        self.main_button.setFixedHeight(80)
        self.main_button.setText('Quay lại màn hình chính')
        self.main_button.clicked.connect(self.goToMainScr)
        self.column_record.addWidget(self.main_button)

        self.widget = QWidget()
        self.widget.setLayout(self.column01)
        self.setCentralWidget(self.widget)

        # self.setStaffName()
    def goToExportScr(self):
        widget_stack.setCurrentWidget(export_screen)
    def goToMainScr(self):
        widget_stack.setCurrentWidget(mainWindow)
    def setTurn(self):
        self.turn.setText('Lượt cân: ' + self.input1.input.text())
    def setPackage(self):
        self.package.setText('Thùng bì: ' + self.input2.input.text())
    def setType(self):
        self.type.setText('Chủng loại phế liệu: ' + self.input3.input.text())
    def setTurnInfo(self):
        self.turn_info.setText('Thông tin lượt cân: ' + self.input4.input.text())



if __name__ == "__main__":
    # create pyqt5 app
    app = QApplication(sys.argv)
    widget_stack = QStackedWidget()
    widget_stack.setWindowTitle('Waste Management')

    mainWindow = MainWindow()
    import_screen = Import_screen()
    export_screen = ExportScreen()
    export_screen_info = ExportScreenInfo()


    widget_stack.addWidget(mainWindow)
    widget_stack.addWidget(import_screen)
    widget_stack.addWidget(export_screen)
    widget_stack.addWidget(export_screen_info)

    widget_stack.showMaximized()
    widget_stack.show()
    # start the app
    sys.exit(app.exec())
