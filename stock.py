# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Documents\Projets\open-breware\stock.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TabStock(object):
    def setupUi(self, TabStock):
        TabStock.setObjectName("TabStock")
        TabStock.resize(400, 300)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(TabStock.sizePolicy().hasHeightForWidth())
        TabStock.setSizePolicy(sizePolicy)
        self.gridLayout = QtWidgets.QGridLayout(TabStock)
        self.gridLayout.setObjectName("gridLayout")
        self.addButton = QtWidgets.QPushButton(TabStock)
        self.addButton.setObjectName("addButton")
        self.gridLayout.addWidget(self.addButton, 2, 0, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(TabStock)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayout.addWidget(self.tableWidget, 1, 0, 1, 1)
        self.itemCategoryScroll = QtWidgets.QComboBox(TabStock)
        self.itemCategoryScroll.setObjectName("itemCategoryScroll")
        self.itemCategoryScroll.addItem("")
        self.itemCategoryScroll.addItem("")
        self.itemCategoryScroll.addItem("")
        self.itemCategoryScroll.addItem("")
        self.gridLayout.addWidget(self.itemCategoryScroll, 0, 0, 1, 1)
        self.saveButton = QtWidgets.QPushButton(TabStock)
        self.saveButton.setObjectName("saveButton")
        self.gridLayout.addWidget(self.saveButton, 3, 0, 1, 1)

        self.retranslateUi(TabStock)
        QtCore.QMetaObject.connectSlotsByName(TabStock)

    def retranslateUi(self, TabStock):
        _translate = QtCore.QCoreApplication.translate
        TabStock.setWindowTitle(_translate("TabStock", "Form"))
        self.addButton.setText(_translate("TabStock", "Add"))
        self.itemCategoryScroll.setItemText(0, _translate("TabStock", "malt"))
        self.itemCategoryScroll.setItemText(1, _translate("TabStock", "hop"))
        self.itemCategoryScroll.setItemText(2, _translate("TabStock", "yeast"))
        self.itemCategoryScroll.setItemText(3, _translate("TabStock", "others"))
        self.saveButton.setText(_translate("TabStock", "Save"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TabStock = QtWidgets.QWidget()
    ui = Ui_TabStock()
    ui.setupUi(TabStock)
    TabStock.show()
    sys.exit(app.exec_())
