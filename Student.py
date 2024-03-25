from PyQt5.QtWidgets import QTabWidget, QMessageBox, QDialog, QLabel, QTextEdit, QPushButton, QLineEdit
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout
from PyQt5.QtSql import QSqlQueryModel
from PyQt5.QtCore import pyqtSlot

class Model(QSqlQueryModel):
    def __init__(self, parent=None):
        super().__init__(parent)

        sql = '''
            ;
        '''
        self.setQuery(sql)

class View(QTabWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        model = Model(parent=self)
        self.setModel(model)

    @pyqtSlot()
    def add(self):
        dia = Dialog(parent=self)
        dia.exec()

    @pyqtSlot()
    def update(self):
        QMessageBox.information(self, 'Студент', 'Обновить')

    @pyqtSlot()
    def delete(self):
        QMessageBox.information(self, 'Студент', 'Удалить')

class Dialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        fio_lbl = QLabel('Фамилия И. О.', parent=self)
        self.__fio_edt = QLineEdit(parent=self)

        phone_lbl = QLabel('Телефон', parent=self)
        self.__phone_edt = QLineEdit(parent=self)

        email_lbl = QLabel('Email', parent=self)
        self.__email_edt = QLineEdit(parent=self)

        comment_lbl = QLabel('Примечание', parent=self)
        self.__comment_edt = QTextEdit(parent=self)

        ok_btn = QPushButton('ок', parent=self)
        cancel_btn = QPushButton('отмена', parent=self)