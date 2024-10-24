
from PyQt5 import QtCore, QtGui, QtWidgets
from CalendarProject import Ui_PythonCalendar

class Ui_MainWindow(object):
    def createUser(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_PythonCalendar()
        self.ui.setupUi(self.window)
        self.window.show()
    def quitProgram(self):
        QtWidgets.QApplication.quit()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 535)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.titleLabel = QtWidgets.QLabel(self.centralwidget)
        self.titleLabel.setGeometry(QtCore.QRect(80, 0, 651, 221))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.titleLabel.setFont(font)
        self.titleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.titleLabel.setObjectName("titleLabel")
        self.nameLabel = QtWidgets.QLabel(self.centralwidget)
        self.nameLabel.setGeometry(QtCore.QRect(220, 160, 361, 51))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.nameLabel.setFont(font)
        self.nameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.nameLabel.setObjectName("nameLabel")
        self.nameEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.nameEdit.setGeometry(QtCore.QRect(210, 270, 381, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.nameEdit.setFont(font)
        self.nameEdit.setObjectName("nameEdit")
        self.userCreate = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.createUser())
        self.userCreate.setGeometry(QtCore.QRect(260, 360, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.userCreate.setFont(font)
        self.userCreate.setObjectName("userCreate")
        self.quitButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.quitProgram())
        self.quitButton.setGeometry(QtCore.QRect(260, 410, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.quitButton.setFont(font)
        self.quitButton.setObjectName("quitButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
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
        self.titleLabel.setText(_translate("MainWindow", "Welcome to the Python Calendar"))
        self.nameLabel.setText(_translate("MainWindow", "Enter your Name"))
        self.userCreate.setText(_translate("MainWindow", "Create User"))
        self.quitButton.setText(_translate("MainWindow", "Quit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

