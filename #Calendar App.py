
import sys
import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as gui

class Window(qtw.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("The Python Calendar")
        self.setLayout(qtw.QVBoxLayout())
        title_label = qtw.QLabel("Welcome to the Python Calendar Startup! Please enter your name:")
        title_label.setFont(gui.QFont('Arial', 18))

        self.layout().addWidget(title_label)
        entry = qtw.QLineEdit()
        entry.setObjectName("name_entry")
        entry.setText("")
        self.layout().addWidget(entry)

        create_user = qtw.QPushButton("Create User",
        clicked = lambda: created_user())
        self.layout().addWidget(create_user)

        self.show()

        def created_user():
            title_label.setText(f'Welcome {entry.text()}!')
            entry.setText("")
    
application = qtw.QApplication([])
mainWin = Window()



application.exec_()

        
