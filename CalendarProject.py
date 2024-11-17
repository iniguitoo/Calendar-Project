# We relied heavily on PyQt5 and Designer in our beta UI development
import pickle  # Pickle is being used for our open functions
from PyQt5 import QtCore, QtGui, QtWidgets
from EventCreation import Ui_EventMaker
from EventDeletion import Ui_DeleteEvent
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PythonCalendar(object):
    # The UI is set up with the below code
    def setupUi(self, PythonCalendar, username="User"):
        PythonCalendar.setObjectName("PythonCalendar")
        PythonCalendar.resize(904, 859)
        
        # Create central widget and layout for resizing
        self.centralwidget = QtWidgets.QWidget(PythonCalendar)
        self.centralwidget.setObjectName("centralwidget")
        
        # Use QVBoxLayout to manage the layout
        self.layout = QtWidgets.QVBoxLayout(self.centralwidget)

        # Create the calendar widget and set it to the top of the layout
        self.calendar_1 = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendar_1.setObjectName("calendar_1")
        self.layout.addWidget(self.calendar_1)

        # Create the event output label
        self.eventOutput = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Nirmala UI Semilight")
        font.setPointSize(14)
        self.eventOutput.setFont(font)
        self.eventOutput.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.eventOutput.setAlignment(QtCore.Qt.AlignCenter)
        self.eventOutput.setObjectName("eventOutput")
        self.layout.addWidget(self.eventOutput)

        # Create the user name label
        self.userName = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.userName.setFont(font)
        self.userName.setAlignment(QtCore.Qt.AlignCenter)
        self.userName.setObjectName("userName")
        self.layout.addWidget(self.userName)

        # Create the user title label
        self.userTitle = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.userTitle.setFont(font)
        self.userTitle.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.userTitle.setObjectName("userTitle")
        self.layout.addWidget(self.userTitle)

        # Set central widget and menu bar
        PythonCalendar.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(PythonCalendar)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 904, 21))
        self.menubar.setObjectName("menubar")
        self.menufile = QtWidgets.QMenu(self.menubar)
        self.menufile.setObjectName("menufile")
        self.menuShare = QtWidgets.QMenu(self.menufile)
        self.menuShare.setObjectName("menuShare")
        self.menuNew = QtWidgets.QMenu(self.menufile)
        self.menuNew.setObjectName("menuNew")
        self.menuTools = QtWidgets.QMenu(self.menubar)
        self.menuTools.setObjectName("menuTools")
        self.menuEvent = QtWidgets.QMenu(self.menubar)
        self.menuEvent.setObjectName("menuEvent")
        PythonCalendar.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(PythonCalendar)
        self.statusbar.setObjectName("statusbar")
        PythonCalendar.setStatusBar(self.statusbar)

        # Actions and menu setup
        self.actionOpen = QtWidgets.QAction(PythonCalendar)
        self.actionOpen.setObjectName("actionOpen")
        self.actionHoliday = QtWidgets.QAction(PythonCalendar)
        self.actionHoliday.setObjectName("actionHoliday")
        self.actionBirthday = QtWidgets.QAction(PythonCalendar)
        self.actionBirthday.setObjectName("actionBirthday")
        self.actionSave = QtWidgets.QAction(PythonCalendar)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_As = QtWidgets.QAction(PythonCalendar)
        self.actionSave_As.setObjectName("actionSave_As")
        self.actionPreferences = QtWidgets.QAction(PythonCalendar)
        self.actionPreferences.setObjectName("actionPreferences")
        self.actionWidgets = QtWidgets.QAction(PythonCalendar)
        self.actionWidgets.setObjectName("actionWidgets")
        self.actionBeta = QtWidgets.QAction(PythonCalendar)
        self.actionBeta.setObjectName("actionBeta")
        self.actionAdd = QtWidgets.QAction(PythonCalendar)
        self.actionAdd.setObjectName("actionAdd")
        self.actionDelete = QtWidgets.QAction(PythonCalendar)
        self.actionDelete.setObjectName("actionDelete")
        self.actionCalendar = QtWidgets.QAction(PythonCalendar)
        self.actionCalendar.setObjectName("actionCalendar")
        self.actionOpenFile = QtWidgets.QAction(PythonCalendar)
        self.actionOpenFile.setObjectName("actionOpenFile")
        self.menuShare.addAction(self.actionBeta)
        self.menuShare.addSeparator()
        self.menuNew.addAction(self.actionCalendar)
        self.menufile.addAction(self.menuNew.menuAction())
        self.menufile.addAction(self.actionSave)
        self.menufile.addAction(self.actionSave_As)
        self.menufile.addAction(self.actionOpenFile)
        self.menufile.addAction(self.menuShare.menuAction())
        self.menuTools.addAction(self.actionPreferences)
        self.menuTools.addAction(self.actionWidgets)
        self.menuEvent.addAction(self.actionAdd)
        self.menuEvent.addAction(self.actionDelete)
        self.menuEvent.addSeparator()
        self.menubar.addAction(self.menufile.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menuEvent.menuAction())

        self.retranslateUi(PythonCalendar)
        QtCore.QMetaObject.connectSlotsByName(PythonCalendar)

        # Connect actions to functions
        self.actionAdd.triggered.connect(self.openEventWindow)
        self.eventList = []
        self.calendar_1.currentPageChanged.connect(self.monthEventUpdate)
        self.monthEventUpdate()
        self.actionDelete.triggered.connect(self.openDeleteWindow)
        self.actionSave.triggered.connect(self.saveCalendar)
        self.actionOpenFile.triggered.connect(self.loadCalendar)

    def retranslateUi(self, PythonCalendar):
        _translate = QtCore.QCoreApplication.translate
        self.userName.setText(_translate("PythonCalendar", "User"))
        self.userName.setText(_translate("PythonCalendar", "User:"))
        PythonCalendar.setWindowTitle(_translate("PythonCalendar", "Python Calendar"))
        self.eventOutput.setText(_translate("PythonCalendar", "No Events This Month"))
        self.menufile.setTitle(_translate("PythonCalendar", "File"))
        self.menuShare.setTitle(_translate("PythonCalendar", "Share"))
        self.menuNew.setTitle(_translate("PythonCalendar", "New"))
        self.menuTools.setTitle(_translate("PythonCalendar", "Tools"))
        self.menuEvent.setTitle(_translate("PythonCalendar", "Event"))
        self.actionOpen.setText(_translate("PythonCalendar", "Open"))
        self.actionHoliday.setText(_translate("PythonCalendar", "Holiday"))
        self.actionBirthday.setText(_translate("PythonCalendar", "Birthday"))
        self.actionSave.setText(_translate("PythonCalendar", "Save"))
        self.actionSave_As.setText(_translate("PythonCalendar", "Save As"))
        self.actionPreferences.setText(_translate("PythonCalendar", "Preferences"))
        self.actionWidgets.setText(_translate("PythonCalendar", "Widgets"))
        self.actionBeta.setText(_translate("PythonCalendar", "Beta"))
        self.actionAdd.setText(_translate("PythonCalendar", "Add"))
        self.actionDelete.setText(_translate("PythonCalendar", "Delete"))
        self.actionCalendar.setText(_translate("PythonCalendar", "Calendar"))
        self.actionOpenFile.setText(_translate("PythonCalendar", "Open"))

    def openEventWindow(self):  # Opens Event Window
        self.eventWindow = QtWidgets.QMainWindow()
        self.eventUi = Ui_EventMaker()
        self.eventUi.setupUi(self.eventWindow)  # UI Setup
        self.eventUi.createButton.clicked.connect(self.eventAddToCalendar)
        self.eventWindow.show()

    def eventAddToCalendar(self):
        event_name = self.eventUi.eventName.text()  # Adds eventname
        start_date = self.eventUi.dateTimeEditStart.dateTime().toPyDateTime()

        # Store the event in the event list as a tuple
        self.eventList.append((event_name, start_date))

        # Update the eventOutput label
        self.eventOutput.setText("\n".join([f"{e[0]} on {e[1].strftime('%Y-%m-%d')}" for e in self.eventList]))

        self.monthEventUpdate()

        # Highlight the day in the calendar
        highlightDay = QtGui.QTextCharFormat()
        highlightDay.setBackground(QtGui.QBrush(QtGui.QColor("light blue")))
        self.calendar_1.setDateTextFormat(start_date.date(), highlightDay)

        # Close the event window
        self.eventWindow.close()

    def monthEventUpdate(self):
        current_month = self.calendar_1.selectedDate().toString("yyyy-MM")
        month_events = [e for e in self.eventList if e[1].strftime('%Y-%m') == current_month]
        if month_events:
            self.eventOutput.setText("\n".join([f"{e[0]} on {e[1].strftime('%Y-%m-%d')}" for e in month_events]))
        else:
            self.eventOutput.setText("No Events This Month")

    def openDeleteWindow(self):  # Deletes event
        self.deleteWindow = QtWidgets.QMainWindow()
        self.deleteUi = Ui_DeleteEvent()
        self.deleteUi.setupUi(self.deleteWindow)
        self.deleteUi.deleteButton.clicked.connect(self.deleteEvent)
        self.deleteWindow.show()

    def deleteEvent(self):
        event_name = self.deleteUi.eventName.text()  # Get event name to delete
        self.eventList = [e for e in self.eventList if e[0] != event_name]  # Remove the event
        self.monthEventUpdate()  # Update the event output
        self.deleteWindow.close()

    def saveCalendar(self):
        file_name, _ = QtWidgets.QFileDialog.getSaveFileName(None, "Save Calendar", "", "Calendar Files (*.cal);;All Files (*)")
        if file_name:
            with open(file_name, 'wb') as f:
                pickle.dump(self.eventList, f)

    def loadCalendar(self):
        file_name, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Open Calendar", "", "Calendar Files (*.cal);;All Files (*)")
        if file_name:
            with open(file_name, 'rb') as f:
                self.eventList = pickle.load(f)
            self.monthEventUpdate()  # Update events on calendar load


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PythonCalendar = QtWidgets.QMainWindow()
    ui = Ui_PythonCalendar()
    ui.setupUi(PythonCalendar)
    PythonCalendar.show()
    sys.exit(app.exec_())
