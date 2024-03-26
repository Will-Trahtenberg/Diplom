import sys
import sqlite3 as sl
from db_connect import *
import psycopg2
from PyQt5.QtSql import QSqlTableModel, QSqlQuery, QSqlQueryModel, QSqlDatabase
from Application import Application
from MainWindows import MainWindows

app = Application(sys.argv)


def connect(self):
    con = sl.connect('учет студентов.db')

main_windows = MainWindows()
main_windows.showMaximized()

result = app.exec()
sys.exit(result)
