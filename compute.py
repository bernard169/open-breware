# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Documents\Projets\open-breware\compute.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TabCompute(object):
    def setupUi(self, TabCompute):
        TabCompute.setObjectName("TabCompute")
        TabCompute.resize(400, 300)

        self.retranslateUi(TabCompute)
        QtCore.QMetaObject.connectSlotsByName(TabCompute)

    def retranslateUi(self, TabCompute):
        _translate = QtCore.QCoreApplication.translate
        TabCompute.setWindowTitle(_translate("TabCompute", "Form"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TabCompute = QtWidgets.QWidget()
    ui = Ui_TabCompute()
    ui.setupUi(TabCompute)
    TabCompute.show()
    sys.exit(app.exec_())
