from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sys
import json
from mymainwindow import MyMainWindow

database = {"bernard":{"stock": {"malt" : [{"Name" : "Cara gold",
                                            "EBC" : 120,
                                            "Mass" : 860,
                                            "Opening date" : "12.08.2020",
                                            "Notes" : ""},
                                        {"Name" : "Malt acide",
                                        "EBC" : 9,
                                        "Mass" : 930,
                                        "Opening date" : "12.08.2020",
                                        "Notes" : "5% max, malt special"
                                        },
                                        {"Name" : "Malt pilsen",
                                        "EBC" : 4.5,
                                        "Mass" : 900,
                                        "Opening date" : "12.08.2020",
                                        "Notes" : "malt de base"}],
                                    "hop" : [{"Name" : "Amarillo",
                                            "Alpha acid" : 6.5,
                                            "Mass" : 50,
                                            "Opening date" : "12.08.2020",
                                            "Notes" : ""}],
                                    "yeast" : [],
                                    "others" : []},
                        "recepe" : []}}

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mw = QtWidgets.QMainWindow()
    ui = MyMainWindow()
    ui.setupUi(mw, database)
    mw.show()
    sys.exit(app.exec_())