# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Documents\Projets\open-breware\recepe.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TabRecepe(object):
    def setupUi(self, TabRecepe):
        TabRecepe.setObjectName("TabRecepe")
        TabRecepe.resize(400, 300)
        self.label = QtWidgets.QLabel(TabRecepe)
        self.label.setGeometry(QtCore.QRect(200, 160, 56, 16))
        self.label.setObjectName("label")

        self.retranslateUi(TabRecepe)
        QtCore.QMetaObject.connectSlotsByName(TabRecepe)

    def retranslateUi(self, TabRecepe):
        _translate = QtCore.QCoreApplication.translate
        TabRecepe.setWindowTitle(_translate("TabRecepe", "Form"))
        self.label.setText(_translate("TabRecepe", "Recepe"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TabRecepe = QtWidgets.QWidget()
    ui = Ui_TabRecepe()
    ui.setupUi(TabRecepe)
    TabRecepe.show()
    sys.exit(app.exec_())
