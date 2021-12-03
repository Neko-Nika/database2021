import sys
from PyQt5 import QtWidgets
from application import MainWindow
from database import DataBase

def start():
    app = QtWidgets.QApplication(sys.argv)

    window = MainWindow()
    window.show()
    app.exec_()

    # db = DataBase('user1', '123', 'asu')
    # db.add_creator('A', '1', '29.11.2021')
    # db.add_creator('B', '2', '29.11.2021')
    # db.add_creator('C', '3', '29.11.2021')

if __name__ == '__main__':
    start()