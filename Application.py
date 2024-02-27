import sys
import psycopg2
from PyQt5 import QtSql
from PyQt5.QtWidgets import QApplication
from PyQt5.QtSql import QSqlDatabase
import db_connect as dbconn

class Application(QApplication):
    def __init__(self, argv):
        super().__init__(argv)

        db = QSqlDatabase.addDatabase('QPSQL')
        db.setHostName(dbconn.db_params['host'])
        db.setDatabaseName(dbconn.db_params['database'])
        db.setPort(dbconn.db_params['port'])
        db.setUserName(dbconn.db_params['user'])
        db.setPassword(dbconn.db_params['password'])
        ok = db.open()
        if ok:
            print('ok')
            db.close()
        else:
            print('no')

