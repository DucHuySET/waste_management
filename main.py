# This Python file uses the following encoding: utf-8
import sys
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QLine, QRect
from PyQt5.QtGui import QFont, QIcon

from ui.screen.import_screen import *
from ui.screen.export_screen import *
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

if __name__ == "__main__":
    # create pyqt5 app
    app = QApplication(sys.argv)
    widget_stack = QStackedWidget()
    widget_stack.setWindowTitle('Waste Management')

    mainWindow = MainWindow()
    import_screen = Import_screen()
    export_screen = ExportScreen()



    widget_stack.addWidget(mainWindow)
    widget_stack.addWidget(import_screen)
    widget_stack.addWidget(export_screen)

    widget_stack.showMaximized()
    widget_stack.show()
    # start the app
    sys.exit(app.exec())
