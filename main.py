import sys
import sqlite3
from PyQt5 import uic
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
from PyQt5.QtWidgets import QMainWindow, QApplication
from main1 import Ui_MainWindow
from addEditCoffeeForm import Ui_MainWindow_1
import data

con = sqlite3.connect("data/coffee.sqlite")  # Устанавливаем соединение с базой данных
cur = con.cursor()


class CoffeeBase(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        db = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('data/coffee.sqlite')
        db.open()
        self.pushButton.clicked.connect(self.add_edit)
        model = QSqlTableModel(self, db)
        model.setTable('coffee')
        model.select()
        self.tableView.setModel(model)

    def add_edit(self):
        self.okno = AddEdit()
        self.okno.show()
        self.close()


class AddEdit(QMainWindow, Ui_MainWindow_1):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.edit)

    def edit(self):
        colms = self.lineEdit_2.text().split(',')
        reds = self.lineEdit_3.text().split(';')
        for i in range(len(colms)):
            que = f'UPDATE coffee SET {colms[i]} = ? WHERE ID = ?'
            cur.execute(que, (reds[i], self.lineEdit.text(),))
            con.commit()
        if self.lineEdit_4.text() != '':
            to_add = (self.lineEdit_4.text(), self.lineEdit_5.text(), self.lineEdit_6.text(), self.lineEdit_7.text(),
                      self.plainTextEdit.toPlainText(), self.lineEdit_8.text(), self.lineEdit_9.text(),)
            cur.execute('''INSERT INTO coffee VALUES (?, ?, ?, ?, ?, ?, ?)''', to_add)
            con.commit()
        self.m_okno = CoffeeBase()
        self.m_okno.show()
        self.close()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CoffeeBase()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
