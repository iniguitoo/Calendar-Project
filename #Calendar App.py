
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (
    QApplication, 
    QMainWindow,
    QCheckBox,
    QComboBox,
    QDateEdit,
    QDateTimeEdit,
    QDial,
    QDoubleSpinBox,
    QFontComboBox,
    QLabel,
    QLCDNumber,
    QLineEdit,
    QProgressBar,
    QPushButton,
    QRadioButton,
    QSlider,
    QSpinBox,
    QTimeEdit,
    QVBoxLayout,
    QWidget,
)

def app():
    application = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    window.setGeometry(0, 0, 2000, 2000)
    window.setWindowTitle("The Python Calendar")
    widget = QLabel("Test")
    font = widget.font()
    font.setPointSize(70)
    widget.setFont(font)
    widget.setAlignment
  
    window.show()
    sys.exit(application.exec_())

app()
