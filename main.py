import sys

from PyQt5 import uic
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
from PyQt5.QtWidgets import QMainWindow, QTableView, QApplication


class CoffeeBase(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)

        db = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('coffee.sqlite')
        db.open()

        model = QSqlTableModel(self, db)
        model.setTable('coffee')
        model.select()
        self.tableView.setModel(model)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CoffeeBase()
    ex.show()
    sys.exit(app.exec())
