# We relied heavily on PyQt5 and Designer in our beta UI development
from PyQt5 import QtCore, QtGui, QtWidgets
from CalendarProject import Ui_PythonCalendar

class Ui_MainWindow(object):
    def createUser(self):  # Function to pass the user's name to the next window
        username = self.nameEdit.text()
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_PythonCalendar()

        self.ui.setupUi(self.window, username=username)
        self.ui.userName.setText(username)
        self.window.show()
        QtWidgets.QApplication.instance().activeWindow().close()

    def quitProgram(self):
        QtWidgets.QApplication.quit()  # Quit button functionality

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 535)

        # Central widget and main layout
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Outer vertical layout to center all content
        self.outer_layout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.outer_layout.setAlignment(QtCore.Qt.AlignCenter)

        # Inner vertical layout for title and fields
        self.inner_layout = QtWidgets.QVBoxLayout()
        self.inner_layout.setSpacing(20)  # Add spacing between widgets

        # Title label
        self.titleLabel = QtWidgets.QLabel("Welcome to the Python Calendar")
        title_font = QtGui.QFont("Arial", 28, QtGui.QFont.Bold)  
        self.titleLabel.setFont(title_font)
        self.titleLabel.setAlignment(QtCore.Qt.AlignCenter)

        # Name label
        self.nameLabel = QtWidgets.QLabel("Enter your Name")
        label_font = QtGui.QFont("Arial", 20)  
        self.nameLabel.setFont(label_font)
        self.nameLabel.setAlignment(QtCore.Qt.AlignCenter)

        # Name input field with fixed width
        self.nameEdit = QtWidgets.QLineEdit()
        input_font = QtGui.QFont("Arial", 14)
        self.nameEdit.setFont(input_font)
        self.nameEdit.setFixedWidth(400)  

        # User creation button with fixed width
        self.userCreate = QtWidgets.QPushButton("Create User", clicked=self.createUser)
        button_font = QtGui.QFont("Arial", 12, QtGui.QFont.Bold)
        self.userCreate.setFont(button_font)
        self.userCreate.setFixedWidth(200)  
        # Quit button with fixed width
        self.quitButton = QtWidgets.QPushButton("Quit", clicked=self.quitProgram)
        self.quitButton.setFont(button_font)
        self.quitButton.setFixedWidth(200)  

        # Adding widgets to inner layout with spacing
        self.inner_layout.addWidget(self.titleLabel)
        self.inner_layout.addSpacing(10)  
        self.inner_layout.addWidget(self.nameLabel)
        self.inner_layout.addWidget(self.nameEdit, alignment=QtCore.Qt.AlignCenter)
        self.inner_layout.addWidget(self.userCreate, alignment=QtCore.Qt.AlignCenter)
        self.inner_layout.addWidget(self.quitButton, alignment=QtCore.Qt.AlignCenter)

        # Add inner layout to the outer layout
        self.outer_layout.addLayout(self.inner_layout)

        MainWindow.setCentralWidget(self.centralwidget)

        # Menubar and statusbar
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
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
