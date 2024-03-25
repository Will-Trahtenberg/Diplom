from PyQt5.QtWidgets import QMainWindow, QMessageBox
from MainMenu import MainMenu
from PyQt5.QtCore import pyqtSlot

class MainWindows(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        main_menu = MainMenu(parent=self)
        self.setMenuBar(main_menu)

        main_menu.about_qt.triggered.connect(self.about_qt)
        main_menu.about.triggered.connect(self.about)


    @pyqtSlot()
    def about(self):
        title = 'Упралвение для преподавателей'
        text = 'программа для управления над студентам'
        QMessageBox.about(self, title, text)

    @pyqtSlot()
    def about_qt(self):
        QMessageBox.aboutQt(self, 'Управление для преподавателей')


#delete then