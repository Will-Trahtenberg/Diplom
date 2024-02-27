from PyQt5.QtWidgets import QTabWidget, QMessageBox, QDialog, QLabel, QTextEdit, QPushButton, QLineEdit
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout
from PyQt5.QtSql import QSqlQueryModel
from PyQt5.QtSql import QSqlQueryModel
from PyQt5.QtCore import pyqtSlot

class Model(QSqlQueryModel):
    def __init__(self, parent=None):
        super().__init__(parent)

        sql = '''
            select id, фио, дата рождения, адрес проживания, номер телефона, номер зачетной книжки, 
            статус, дата поступления, дата окончания, номер диплома, код группы, пол
            from студент ;
        '''
        self.setQuery(sql)

class View(QTabWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        model = Model(parent=self)
        self.setModel(model)

    @pyqtSlot()
    def add(self):
        QMessageBox.information(self, 'Студент', 'Добавить')

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
        self.__fio_edit = QLineEdit(parent=self)

