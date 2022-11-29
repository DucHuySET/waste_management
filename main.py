# This Python file uses the following encoding: utf-8
import sys
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QLine, QRect, pyqtSlot, pyqtSignal
from PyQt5.QtGui import QFont, QIcon

from ui.screen.import_screen import *
from ui.screen.export_screen import *
from ui.screen.export_screen_info import *
from ui.screen.main_screen import *
from ui.base_widget.utils_widget import *

def main():
    app = QApplication(sys.argv)
    widget_stack = QStackedWidget()
    widget_stack.setWindowTitle('Quản lý nhập - xuất phế liệu')
    widget_stack.setWindowIcon(QIcon('D:/Qt/Project/Test_Qt_Creator/assets/images/CTARG.png'))
    app.setStyleSheet('QApplication{background-color: yellow; color: blue}')

    mainWindow = MainWindow()
    import_screen = Import_screen(widget_stack, mainWindow)
    export_screen = ExportScreen(widget_stack, mainWindow)
    export_screen_info = ExportScreenInfo(widget_stack, mainWindow, export_screen)

    def goToImportScr():
        widget_stack.setCurrentWidget(import_screen)
    mainWindow.button_import.clicked.connect(goToImportScr)

    def goToExportScr():
        widget_stack.setCurrentWidget(export_screen)
    mainWindow.button_export.clicked.connect(goToExportScr)


    def goToInfoScr():
        widget_stack.setCurrentWidget(export_screen_info)
    export_screen.next_button.clicked.connect(goToInfoScr)

    widget_stack.addWidget(mainWindow)
    widget_stack.addWidget(import_screen)
    widget_stack.addWidget(export_screen)
    widget_stack.addWidget(export_screen_info)

    widget_stack.showMaximized()
    widget_stack.show()
    # start the app
    sys.exit(app.exec())



if __name__ == "__main__":
    main()