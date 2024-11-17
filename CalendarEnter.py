# We relied heavily on PyQt5 and Designer in our beta UI development
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QFontDatabase
from CalendarProject import Ui_PythonCalendar

class Ui_MainWindow(object):
    def __init__(self):
        regular_font_id = QFontDatabase.addApplicationFont("fonts/ProductSans-Regular.ttf")
        if regular_font_id == -1:
            print("Failed to load Product Sans Regular font.")
        else:
            self.product_sans_regular = QFontDatabase.applicationFontFamilies(regular_font_id)[0]  # Regular font family

        medium_font_id = QFontDatabase.addApplicationFont("fonts/ProductSans-Medium.ttf")
        if medium_font_id == -1:
            print("Failed to load Product Sans Medium font.")
        else:
            self.product_sans_medium = QFontDatabase.applicationFontFamilies(medium_font_id)[0]  # Medium font family
        
        thin_font_id = QFontDatabase.addApplicationFont("fonts/ProductSans-Thin.ttf")
        if thin_font_id == -1:
            print("Failed to load Product Sans Thin font.")
        else:
            self.product_sans_thin = QFontDatabase.applicationFontFamilies(thin_font_id)[0]  # Thin font family

    def createUser(self):  # Function to pass the user's name to the next window
        username = self.nameEdit.text()

        if not username:  # Check if the input is empty
            self.errorLabel.setText("Please, enter your name")  # Show error message
            self.errorLabel.setVisible(True)  # Make error label visible
        else:
            self.errorLabel.setText("")  # Clear any existing error messages
            self.errorLabel.setVisible(False)  # Hide the error label
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
        self.inner_layout.setSpacing(30)  # Add spacing between widgets

        # Title label with highlighted "Python Calendar"
        self.titleLabel = QtWidgets.QLabel()
        title_font = QtGui.QFont(self.product_sans_medium, 28, QtGui.QFont.Bold)
        self.titleLabel.setFont(title_font)
        self.titleLabel.setAlignment(QtCore.Qt.AlignCenter)

        # Set rich text for title with primary color highlight
        self.titleLabel.setText(
            '<span style="font-size:28pt; font-weight:bold; font-family:\'Product Sans Medium\';">'
            'Welcome to the <span style="background-color:#03a9f4; color:white; padding:5px;">Python Calendar!</span>'
            '</span>'
        )

        # Name label
        self.nameLabel = QtWidgets.QLabel("Enter your Name")
        label_font = QtGui.QFont(self.product_sans_regular, 20)
        self.nameLabel.setFont(label_font)
        self.nameLabel.setAlignment(QtCore.Qt.AlignCenter)

        # Name input field with fixed width
        self.nameEdit = QtWidgets.QLineEdit()
        input_font = QtGui.QFont(self.product_sans_regular, 14)
        self.nameEdit.setFont(input_font)
        self.nameEdit.setFixedWidth(400)

        # Error message label (Now between input and button)
        self.errorLabel = QtWidgets.QLabel()  # Label for error message
        self.errorLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.errorLabel.setStyleSheet("color: red;")  
        self.errorLabel.setFont(QtGui.QFont(self.product_sans_thin, 10))  
        self.errorLabel.setVisible(False)  # Initially hidden

        # User creation button with primary color and shadow
        self.userCreate = QtWidgets.QPushButton("Create User", clicked=self.createUser)
        button_font = QtGui.QFont(self.product_sans_regular, 12, QtGui.QFont.Bold)
        self.userCreate.setFont(button_font)
        self.userCreate.setFixedWidth(200)
        self.userCreate.setStyleSheet(
            "QPushButton {"
            "background-color: #03a9f4; color: white; border-radius: 5px; padding: 10px;"
            "}"
        )
        # Quit button with secondary color and shadow
        self.quitButton = QtWidgets.QPushButton("Quit", clicked=self.quitProgram)
        self.quitButton.setFont(button_font)
        self.quitButton.setFixedWidth(200)
        self.quitButton.setStyleSheet(
            "QPushButton {"
            "background-color: #757575; color: white; border-radius: 5px; padding: 10px;"
            "}"
        )

        # Adding widgets to inner layout with spacing
        self.inner_layout.addWidget(self.titleLabel)
        self.inner_layout.addSpacing(10)
        self.inner_layout.addWidget(self.nameLabel)
        self.inner_layout.addWidget(self.nameEdit, alignment=QtCore.Qt.AlignCenter)
        self.inner_layout.addWidget(self.errorLabel, alignment=QtCore.Qt.AlignCenter)  # Error message between input and button
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
        self.nameLabel.setText(_translate("MainWindow", "Enter your Name"))
        self.userCreate.setText(_translate("MainWindow", "Create User"))
        self.quitButton.setText(_translate("MainWindow", "Quit"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")  # Ensure the Fusion style is used to support hover
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
