<<<<<<< HEAD
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CalendarEnter.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(776, 380)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.enterNameLabel1 = QtWidgets.QLabel(self.centralwidget)
        self.enterNameLabel1.setGeometry(QtCore.QRect(-20, 0, 821, 141))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.enterNameLabel1.setFont(font)
        self.enterNameLabel1.setAlignment(QtCore.Qt.AlignCenter)
        self.enterNameLabel1.setObjectName("enterNameLabel1")
        self.enterNameLabel2 = QtWidgets.QLabel(self.centralwidget)
        self.enterNameLabel2.setGeometry(QtCore.QRect(110, 100, 571, 101))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.enterNameLabel2.setFont(font)
        self.enterNameLabel2.setAlignment(QtCore.Qt.AlignCenter)
        self.enterNameLabel2.setObjectName("enterNameLabel2")
        self.nameEntry = QtWidgets.QLineEdit(self.centralwidget)
        self.nameEntry.setGeometry(QtCore.QRect(150, 200, 481, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.nameEntry.setFont(font)
        self.nameEntry.setAlignment(QtCore.Qt.AlignCenter)
        self.nameEntry.setObjectName("nameEntry")
        self.createUser = QtWidgets.QPushButton(self.centralwidget)
        self.createUser.setGeometry(QtCore.QRect(300, 260, 171, 23))
        self.createUser.setObjectName("createUser")
        self.quitButton = QtWidgets.QPushButton(self.centralwidget)
        self.quitButton.setGeometry(QtCore.QRect(300, 290, 171, 23))
        self.quitButton.setObjectName("quitButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 776, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.enterNameLabel1.setText(_translate("MainWindow", "Welcome to the Python Calendar!"))
        self.enterNameLabel2.setText(_translate("MainWindow", "Enter Your Name to Get Started"))
        self.createUser.setText(_translate("MainWindow", "Create User"))
        self.quitButton.setText(_translate("MainWindow", "Quit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
=======
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CalendarEnter.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(778, 354)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.enterNameLabel1 = QtWidgets.QLabel(self.centralwidget)
        self.enterNameLabel1.setGeometry(QtCore.QRect(-20, 0, 821, 141))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.enterNameLabel1.setFont(font)
        self.enterNameLabel1.setAlignment(QtCore.Qt.AlignCenter)
        self.enterNameLabel1.setObjectName("enterNameLabel1")
        self.enterNameLabel2 = QtWidgets.QLabel(self.centralwidget)
        self.enterNameLabel2.setGeometry(QtCore.QRect(110, 100, 571, 101))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.enterNameLabel2.setFont(font)
        self.enterNameLabel2.setAlignment(QtCore.Qt.AlignCenter)
        self.enterNameLabel2.setObjectName("enterNameLabel2")
        self.nameEntry = QtWidgets.QLineEdit(self.centralwidget)
        self.nameEntry.setGeometry(QtCore.QRect(150, 200, 481, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.nameEntry.setFont(font)
        self.nameEntry.setAlignment(QtCore.Qt.AlignCenter)
        self.nameEntry.setObjectName("nameEntry")
        self.createUser = QtWidgets.QPushButton(self.centralwidget)
        self.createUser.setGeometry(QtCore.QRect(300, 260, 171, 23))
        self.createUser.setObjectName("createUser")
        self.quitButton = QtWidgets.QPushButton(self.centralwidget)
        self.quitButton.setGeometry(QtCore.QRect(300, 290, 171, 23))
        self.quitButton.setObjectName("quitButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 778, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.enterNameLabel1.setText(_translate("MainWindow", "Welcome to the Python Calendar!"))
        self.enterNameLabel2.setText(_translate("MainWindow", "Enter Your Name to Get Started"))
        self.createUser.setText(_translate("MainWindow", "Create User"))
        self.quitButton.setText(_translate("MainWindow", "Quit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
>>>>>>> b4ae3ab368bf0b6cd87bb46fde941ee442643870
