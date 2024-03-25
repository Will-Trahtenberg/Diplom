import psycopg2
from PyQt5.QtWidgets import QApplication
from PyQt5.QtSql import QSqlDatabase, QSqlQueryModel, QSqlQuery, QSqlTableModel
import db_connect as dbconn

class Application(QApplication):
    def __init__(self, argv):
        super().__init__(argv)

        db = QSqlDatabase.addDatabase('postgres')
        db.setHostName(dbconn.db_params['host'])
        db.setDatabaseName(dbconn.db_params['database'])
        db.setPort(dbconn.db_params['port'])
        db.setUserName(dbconn.db_params['user'])
        db.setPassword(dbconn.db_params['password'])

    def connect(self):
        self.connect = connection = psycopg2.connect(
            host='localhost',
            port=5432,
            database='учет студентов',
            password='12345678',
            user='postgres'
        )
        self.cur = self.connect.cursor()

class Table():
    def __init__(self):
        super().__init__()