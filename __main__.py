import sys
from db_connect import *
import psycopg2
from PyQt5.QtSql import QSqlTableModel, QSqlQuery, QSqlQueryModel, QSqlDatabase
from Application import Application
from MainWindows import MainWindows

app = Application(sys.argv)


def connect(self):
    self.connect = connection = psycopg2.connect(
        host='localhost',
        port=5432,
        database='учет студентов',
        password='12345678',
        user='postgres'
    )
    self.cur = self.connect.cursor()

main_windows = MainWindows()
main_windows.showMaximized()

result = app.exec()
sys.exit(result)
