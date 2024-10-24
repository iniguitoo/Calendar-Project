#We relied heavily on PyQt5 and Designer in our beta UI development
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_EventMaker(object):
    def setupUi(self, EventMaker):
        EventMaker.setObjectName("EventMaker")
        EventMaker.resize(422, 345)
        self.centralwidget = QtWidgets.QWidget(EventMaker)
        self.centralwidget.setObjectName("centralwidget")
        self.titleLabel = QtWidgets.QLabel(self.centralwidget)
        self.titleLabel.setGeometry(QtCore.QRect(20, 10, 381, 71))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.titleLabel.setFont(font)
        self.titleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.titleLabel.setObjectName("titleLabel")
        self.startLabel = QtWidgets.QLabel(self.centralwidget)
        self.startLabel.setGeometry(QtCore.QRect(20, 100, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.startLabel.setFont(font)
        self.startLabel.setObjectName("startLabel")
        self.dateTimeEditStart = QtWidgets.QDateTimeEdit(self.centralwidget)
        self.dateTimeEditStart.setGeometry(QtCore.QRect(210, 101, 201, 31))
        self.dateTimeEditStart.setObjectName("dateTimeEditStart")
        self.endLabel = QtWidgets.QLabel(self.centralwidget)
        self.endLabel.setGeometry(QtCore.QRect(20, 150, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.endLabel.setFont(font)
        self.endLabel.setObjectName("endLabel")
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.centralwidget)
        self.dateTimeEdit.setGeometry(QtCore.QRect(210, 160, 201, 31))
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.eventName = QtWidgets.QLineEdit(self.centralwidget)
        self.eventName.setGeometry(QtCore.QRect(110, 210, 191, 31))
        self.eventName.setAlignment(QtCore.Qt.AlignCenter)
        self.eventName.setObjectName("eventName")
        self.createButton = QtWidgets.QPushButton(self.centralwidget)
        self.createButton.setGeometry(QtCore.QRect(160, 260, 91, 31))
        self.createButton.setObjectName("createButton")
        EventMaker.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(EventMaker)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 422, 21))
        self.menubar.setObjectName("menubar")
        EventMaker.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(EventMaker)
        self.statusbar.setObjectName("statusbar")
        EventMaker.setStatusBar(self.statusbar)

        self.retranslateUi(EventMaker)
        QtCore.QMetaObject.connectSlotsByName(EventMaker)

    def retranslateUi(self, EventMaker):
        _translate = QtCore.QCoreApplication.translate
        EventMaker.setWindowTitle(_translate("EventMaker", "MainWindow"))
        self.titleLabel.setText(_translate("EventMaker", "Create an Event..."))
        self.startLabel.setText(_translate("EventMaker", "Start Date and Time:"))
        self.endLabel.setText(_translate("EventMaker", "End Date and Time:"))
        self.eventName.setText(_translate("EventMaker", "Event Name..."))
        self.createButton.setText(_translate("EventMaker", "Create Event"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    EventMaker = QtWidgets.QMainWindow()
    ui = Ui_EventMaker()
    ui.setupUi(EventMaker)
    EventMaker.show()
    sys.exit(app.exec_())
