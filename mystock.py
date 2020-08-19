from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sys
import json
import stock

class MyStock(stock.Ui_TabStock):
    def setupUi(self, widget, stock):
        super().setupUi(widget)
        self.stock = stock
        self.headers = []
        self.setContent()
        self.itemCategoryScroll.currentIndexChanged.connect(self.setContent)
        self.saveButton.clicked.connect(self.save)
        self.addButton.clicked.connect(self.add)                                           
        
    def setContent(self):
        if self.itemCategoryScroll.currentIndex() is 0:
            content = self.stock["malt"]
        elif self.itemCategoryScroll.currentIndex() is 1:
            content = self.stock["hop"]
        elif self.itemCategoryScroll.currentIndex() is 2:
            content = self.stock["yeast"]
        self.tableWidget.setColumnCount(len(content[0]))
        self.tableWidget.setRowCount(len(content))
        self.headers = list(content[0].keys())
        print (self.headers)
        self.tableWidget.setHorizontalHeaderLabels(self.headers)
        row = 0
        for item in content:
            for entry in item.keys():
                column = 0
                while column < len(self.headers):
                    #if QtWidgets.QTableWidgetItem(entry) == self.tableWidget.horizontalHeaderItem(column):
                    if str(entry) == self.headers[column]:
                        print("HELLO MOTHERFUCKER\n")
                        break
                    else :
                        column += 1
                else: # python is cool :)
                    print("Cannot find specified header")
                print(QtWidgets.QTableWidgetItem(item[entry]))
                self.tableWidget.setItem(row, column ,QtWidgets.QTableWidgetItem(str(item[entry])))
            row += 1

    def save(self):
        pass

    def add(self):
        pass