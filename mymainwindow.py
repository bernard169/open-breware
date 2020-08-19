from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sys
import json
import mainwindow, mystock, recepe, compute

class MyMainWindow(mainwindow.Ui_MainWindow):
    def setupUi(self, mw, database):
        super().setupUi(mw)
        self.tabWidget = QtWidgets.QTabWidget()
        mw.setCentralWidget(self.tabWidget)
        self.ms = QtWidgets.QWidget()
        self.mystock = mystock.MyStock()
        self.mystock.setupUi(self.ms, database["bernard"]["stock"])
        self.tabWidget.addTab(self.ms, "STOCK")
        self.mr = QtWidgets.QWidget()
        self.myRecepe = recepe.Ui_TabRecepe()
        self.myRecepe.setupUi(self.mr)
        self.tabWidget.addTab(self.mr, "Recepe")
        self.mc = QtWidgets.QWidget()
        self.myCompute = compute.Ui_TabCompute()
        self.myCompute.setupUi(self.mc)
        self.tabWidget.addTab(self.mc, "Compute")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mw = QtWidgets.QMainWindow()
    ui = MyMainWindow()
    ui.setupUi(mw)
    mw.show()
    sys.exit(app.exec_())