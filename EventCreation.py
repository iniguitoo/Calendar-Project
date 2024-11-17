from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QFontDatabase

class Ui_EventMaker(object):
    def __init__(self):
        # Load fonts (Product Sans Regular, Medium, and Thin)
        regular_font_id = QFontDatabase.addApplicationFont("fonts/ProductSans-Regular.ttf")
        if regular_font_id == -1:
            print("Failed to load Product Sans Regular font.")
        else:
            self.product_sans_regular = QFontDatabase.applicationFontFamilies(regular_font_id)[0]

        medium_font_id = QFontDatabase.addApplicationFont("fonts/ProductSans-Medium.ttf")
        if medium_font_id == -1:
            print("Failed to load Product Sans Medium font.")
        else:
            self.product_sans_medium = QFontDatabase.applicationFontFamilies(medium_font_id)[0]
        
        thin_font_id = QFontDatabase.addApplicationFont("fonts/ProductSans-Thin.ttf")
        if thin_font_id == -1:
            print("Failed to load Product Sans Thin font.")
        else:
            self.product_sans_thin = QFontDatabase.applicationFontFamilies(thin_font_id)[0]

    def setupUi(self, EventMaker):
        EventMaker.setObjectName("EventMaker")
        EventMaker.resize(422, 345)

        self.centralwidget = QtWidgets.QWidget(EventMaker)
        self.centralwidget.setObjectName("centralwidget")

        # Main vertical layout
        self.mainLayout = QtWidgets.QVBoxLayout(self.centralwidget)

        # Add vertical stretch before the content (to center it vertically)
        self.mainLayout.addStretch(1)

        # Title label (centered horizontally)
        self.titleLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont(self.product_sans_medium, 22, QtGui.QFont.Bold)
        self.titleLabel.setFont(font)
        self.titleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.titleLabel.setText("Create an Event")
        self.mainLayout.addWidget(self.titleLabel)

        # Add some spacing between the title and the next section
        self.mainLayout.addSpacing(20)

        # Start Date and Time label and input (centered horizontally)
        self.startLabel = QtWidgets.QLabel(self.centralwidget)
        font.setPointSize(12)
        self.startLabel.setFont(font)
        self.startLabel.setText("Start Date and Time:")

        self.startLayout = QtWidgets.QHBoxLayout()
        self.startLayout.addStretch(1)
        self.startLayout.addWidget(self.startLabel)
        self.startLayout.addStretch(1)
        self.mainLayout.addLayout(self.startLayout)

        # Start Date and Time picker (centered horizontally)
        self.dateTimeEditStart = QtWidgets.QDateTimeEdit(self.centralwidget)
        self.dateTimeEditStart.setMinimumHeight(40)
        self.dateTimeEditStart.setMaximumWidth(250)
        self.dateTimeEditStart.setFont(QtGui.QFont(self.product_sans_regular, 14))
        self.dateTimeEditStart.setDateTime(QtCore.QDateTime.currentDateTime())

        self.dateTimeLayoutStart = QtWidgets.QHBoxLayout()
        self.dateTimeLayoutStart.addStretch(1)
        self.dateTimeLayoutStart.addWidget(self.dateTimeEditStart)
        self.dateTimeLayoutStart.addStretch(1)
        self.mainLayout.addLayout(self.dateTimeLayoutStart)

        # Add vertical spacing
        self.mainLayout.addSpacing(20)

        # End Date and Time label and input (centered horizontally)
        self.endLabel = QtWidgets.QLabel(self.centralwidget)
        self.endLabel.setFont(font)
        self.endLabel.setText("End Date and Time:")

        self.endLayout = QtWidgets.QHBoxLayout()
        self.endLayout.addStretch(1)
        self.endLayout.addWidget(self.endLabel)
        self.endLayout.addStretch(1)
        self.mainLayout.addLayout(self.endLayout)

        # End Date and Time picker
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.centralwidget)
        self.dateTimeEdit.setMinimumHeight(40)
        self.dateTimeEdit.setMaximumWidth(250)
        self.dateTimeEdit.setFont(QtGui.QFont(self.product_sans_regular, 14))
        self.dateTimeEdit.setDateTime(QtCore.QDateTime.currentDateTime())

        self.dateTimeLayout = QtWidgets.QHBoxLayout()
        self.dateTimeLayout.addStretch(1)
        self.dateTimeLayout.addWidget(self.dateTimeEdit)
        self.dateTimeLayout.addStretch(1)
        self.mainLayout.addLayout(self.dateTimeLayout)

        # Add vertical spacing
        self.mainLayout.addSpacing(20)

        # Event Name input (centered horizontally)
        self.eventName = QtWidgets.QLineEdit(self.centralwidget)
        self.eventName.setAlignment(QtCore.Qt.AlignCenter)
        self.eventName.setPlaceholderText("Event Name")
        self.eventName.setMaximumWidth(200)
        self.eventName.setFont(QtGui.QFont(self.product_sans_regular, 14))

        self.nameLayout = QtWidgets.QHBoxLayout()
        self.nameLayout.addStretch(1)
        self.nameLayout.addWidget(self.eventName)
        self.nameLayout.addStretch(1)
        self.mainLayout.addLayout(self.nameLayout)

        # Error message label
        self.errorLabel = QtWidgets.QLabel(self.centralwidget)
        self.errorLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.errorLabel.setStyleSheet("color: red;")
        self.errorLabel.setFont(QtGui.QFont(self.product_sans_thin, 10))
        self.errorLabel.setVisible(False)

        self.errorLayout = QtWidgets.QHBoxLayout()
        self.errorLayout.addStretch(1)
        self.errorLayout.addWidget(self.errorLabel)
        self.errorLayout.addStretch(1)
        self.mainLayout.addLayout(self.errorLayout)

        # Add vertical spacing
        self.mainLayout.addSpacing(20)

        # Color picker label and button
        self.colorLabel = QtWidgets.QLabel(self.centralwidget)
        self.colorLabel.setFont(font)
        self.colorLabel.setText("Event Color:")

        self.colorLayout = QtWidgets.QHBoxLayout()
        self.colorLayout.addStretch(1)
        self.colorLayout.addWidget(self.colorLabel)
        self.colorLayout.addStretch(1)
        self.mainLayout.addLayout(self.colorLayout)

        # Color picker button
        self.colorButton = QtWidgets.QPushButton(self.centralwidget)
        self.colorButton.setText("Select Color")
        self.colorButton.setMaximumWidth(200)
        self.colorButton.setFont(QtGui.QFont(self.product_sans_regular, 12))
        self.colorButton.setStyleSheet(
            "QPushButton {"
            "background-color: #03a9f4; color: white; border-radius: 5px; padding: 10px;"
            "}"
        )
        self.selectedColor = "#03a9f4"  # Default color

        self.colorButtonLayout = QtWidgets.QHBoxLayout()
        self.colorButtonLayout.addStretch(1)
        self.colorButtonLayout.addWidget(self.colorButton)
        self.colorButtonLayout.addStretch(1)
        self.mainLayout.addLayout(self.colorButtonLayout)

        # Connect color picker button
        self.colorButton.clicked.connect(self.openColorDialog)

        # Add vertical spacing
        self.mainLayout.addSpacing(20)

        # Create Event button
        self.createButton = QtWidgets.QPushButton(self.centralwidget)
        self.createButton.setText("Create Event")
        self.createButton.setMaximumWidth(150)
        self.createButton.setFont(QtGui.QFont(self.product_sans_regular, 12, QtGui.QFont.Bold))
        self.createButton.setStyleSheet(
            "QPushButton {"
            "background-color: #03a9f4; color: white; border-radius: 5px; padding: 10px;"
            "}"
        )
        self.createButton.clicked.connect(self.validateEvent)

        # Add button to layout
        self.buttonLayout = QtWidgets.QHBoxLayout()
        self.buttonLayout.addStretch(1)
        self.buttonLayout.addWidget(self.createButton)
        self.buttonLayout.addStretch(1)
        self.mainLayout.addLayout(self.buttonLayout)

        # Add vertical stretch
        self.mainLayout.addStretch(1)

        EventMaker.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(EventMaker)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 422, 21))
        EventMaker.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(EventMaker)
        EventMaker.setStatusBar(self.statusbar)

        self.retranslateUi(EventMaker)
        QtCore.QMetaObject.connectSlotsByName(EventMaker)

    def validateEvent(self):
        if not self.eventName.text():
            self.errorLabel.setText("Please enter an event name")
            self.errorLabel.setVisible(True)
        else:
            self.errorLabel.setText("")
            self.errorLabel.setVisible(False)
            # Add your event creation logic here

    def openColorDialog(self):
        color = QtWidgets.QColorDialog.getColor()
        if color.isValid():
            self.selectedColor = color.name()
            self.colorButton.setStyleSheet(
                f"QPushButton {{"
                f"background-color: {self.selectedColor}; color: white; "
                f"border-radius: 5px; padding: 10px;"
                f"}}"
            )

    def retranslateUi(self, EventMaker):
        _translate = QtCore.QCoreApplication.translate
        EventMaker.setWindowTitle(_translate("EventMaker", "EventMaker"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    EventMaker = QtWidgets.QMainWindow()
    ui = Ui_EventMaker()
    ui.setupUi(EventMaker)
    EventMaker.show()
    sys.exit(app.exec_())