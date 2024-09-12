
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

def app():
    application = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    window.setGeometry(0, 0, 2000, 2000)
    window.setWindowTitle("The Python Calendar")
    window.show()
    sys.exit(application.exec_())

app()
