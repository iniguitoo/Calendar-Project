from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QFontDatabase

class Ui_DeleteEvent(object):
    def __init__(self):
        # Load fonts
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

    def setupUi(self, DeleteEvent):
        DeleteEvent.setObjectName("DeleteEvent")
        DeleteEvent.resize(407, 386)

        self.centralwidget = QtWidgets.QWidget(DeleteEvent)
        self.centralwidget.setObjectName("centralwidget")

        # Main layout (center the content in the window)
        self.mainLayout = QtWidgets.QVBoxLayout(self.centralwidget)

        # Spacer to push widgets to the center
        self.mainLayout.addStretch(1)

        # Delete Event label with custom font and style
        self.deleteLabel = QtWidgets.QLabel(self.centralwidget)
        title_font = QtGui.QFont(self.product_sans_medium, 22)
        self.deleteLabel.setFont(title_font)
        self.deleteLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.deleteLabel.setText("Delete an Event...")
        self.mainLayout.addWidget(self.deleteLabel)

        # Instruction label with custom font
        self.selectLabel = QtWidgets.QLabel(self.centralwidget)
        instruction_font = QtGui.QFont(self.product_sans_regular, 14)
        self.selectLabel.setFont(instruction_font)
        self.selectLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.selectLabel.setText("Select the event you wish to delete:")
        self.mainLayout.addWidget(self.selectLabel)

        # Create a horizontal layout to center the ComboBox
        comboLayout = QtWidgets.QHBoxLayout()
        comboLayout.setAlignment(QtCore.Qt.AlignCenter)

        # ComboBox for selecting event with custom font and fixed width
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        combo_font = QtGui.QFont(self.product_sans_regular, 12)
        self.comboBox.setFont(combo_font)
        self.comboBox.setFixedWidth(300)  # Set a fixed width to prevent it from stretching
        comboLayout.addWidget(self.comboBox)  # Add ComboBox to the horizontal layout

        # Add the combo layout to the main layout
        self.mainLayout.addLayout(comboLayout)

        # Delete Event button with custom styling and centered alignment
        self.deleteButton = QtWidgets.QPushButton(self.centralwidget)
        button_font = QtGui.QFont(self.product_sans_regular, 12, QtGui.QFont.Bold)
        self.deleteButton.setFont(button_font)
        self.deleteButton.setText("Delete Event")
        self.deleteButton.setFixedWidth(200)
        self.deleteButton.setStyleSheet(
            "QPushButton {"
            "background-color: #03a9f4; color: white; border-radius: 5px; padding: 10px;"
            "}"
        )
        self.mainLayout.addWidget(self.deleteButton, alignment=QtCore.Qt.AlignCenter)  # Center the button

        # Spacer to keep content centered vertically
        self.mainLayout.addStretch(1)

        DeleteEvent.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(DeleteEvent)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 407, 21))
        DeleteEvent.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(DeleteEvent)
        DeleteEvent.setStatusBar(self.statusbar)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DeleteEvent = QtWidgets.QMainWindow()
    ui = Ui_DeleteEvent()
    ui.setupUi(DeleteEvent)
    DeleteEvent.show()
    sys.exit(app.exec_())
