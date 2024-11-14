
from PyQt5 import QtCore, QtGui, QtWidgets

#This file is strictly the UI code for the event deletion mini window
class Ui_DeleteEvent(object):
    def setupUi(self, DeleteEvent):
        DeleteEvent.setObjectName("DeleteEvent")
        DeleteEvent.resize(407, 386)
        self.centralwidget = QtWidgets.QWidget(DeleteEvent)
        self.centralwidget.setObjectName("centralwidget")
        self.deleteLabel = QtWidgets.QLabel(self.centralwidget)
        self.deleteLabel.setGeometry(QtCore.QRect(50, 20, 321, 81))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(False)
        font.setWeight(50)
        self.deleteLabel.setFont(font)
        self.deleteLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.deleteLabel.setObjectName("deleteLabel")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(100, 160, 191, 31))
        self.comboBox.setObjectName("comboBox")
        self.selectLabel = QtWidgets.QLabel(self.centralwidget)
        self.selectLabel.setGeometry(QtCore.QRect(0, 90, 411, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.selectLabel.setFont(font)
        self.selectLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.selectLabel.setObjectName("selectLabel")
        self.deleteButton = QtWidgets.QPushButton(self.centralwidget)
        self.deleteButton.setGeometry(QtCore.QRect(150, 250, 91, 31))
        self.deleteButton.setObjectName("deleteButton")
        DeleteEvent.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(DeleteEvent)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 407, 21))
        self.menubar.setObjectName("menubar")
        DeleteEvent.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(DeleteEvent)
        self.statusbar.setObjectName("statusbar")
        DeleteEvent.setStatusBar(self.statusbar)

        self.retranslateUi(DeleteEvent)
        QtCore.QMetaObject.connectSlotsByName(DeleteEvent)

    def retranslateUi(self, DeleteEvent):
        _translate = QtCore.QCoreApplication.translate
        DeleteEvent.setWindowTitle(_translate("DeleteEvent", "Delete Event"))
        self.deleteLabel.setText(_translate("DeleteEvent", "Delete an Event..."))
        self.selectLabel.setText(_translate("DeleteEvent", "Select the event you wish to delete:"))
        self.deleteButton.setText(_translate("Delet eEvent", "Delete Event"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DeleteEvent = QtWidgets.QMainWindow()
    ui = Ui_DeleteEvent()
    ui.setupUi(DeleteEvent)
    DeleteEvent.show()
    sys.exit(app.exec_())
