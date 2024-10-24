
from PyQt5 import QtCore, QtGui, QtWidgets
from EventCreation import Ui_EventMaker


class Ui_PythonCalendar(object):
    def setupUi(self, PythonCalendar):
        PythonCalendar.setObjectName("PythonCalendar")
        PythonCalendar.resize(904, 859)
        self.centralwidget = QtWidgets.QWidget(PythonCalendar)
        self.centralwidget.setObjectName("centralwidget")
        self.calendar_1 = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendar_1.setGeometry(QtCore.QRect(10, 60, 881, 581))
        self.calendar_1.setObjectName("calendar_1")
        self.eventOutput = QtWidgets.QLabel(self.centralwidget)
        self.eventOutput.setGeometry(QtCore.QRect(10, 640, 881, 171))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI Semilight")
        font.setPointSize(14)
        self.eventOutput.setFont(font)
        self.eventOutput.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.eventOutput.setAlignment(QtCore.Qt.AlignCenter)
        self.eventOutput.setObjectName("eventOutput")
        self.userName = QtWidgets.QLabel(self.centralwidget)
        self.userName.setGeometry(QtCore.QRect(700, 0, 211, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.userName.setFont(font)
        self.userName.setAlignment(QtCore.Qt.AlignCenter)
        self.userName.setObjectName("userName")
        self.userTitle = QtWidgets.QLabel(self.centralwidget)
        self.userTitle.setGeometry(QtCore.QRect(690, 0, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.userTitle.setFont(font)
        self.userTitle.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.userTitle.setObjectName("userTitle")
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
        self.menuShare.addAction(self.actionBeta)
        self.menuShare.addSeparator()
        self.menuNew.addAction(self.actionCalendar)
        self.menufile.addAction(self.menuNew.menuAction())
        self.menufile.addAction(self.actionSave)
        self.menufile.addAction(self.actionSave_As)
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

        self.actionAdd.triggered.connect(self.openEventWindow)
        self.eventList = []
        self.calendar_1.currentPageChanged.connect(self.monthEventUpdate)
        self.monthEventUpdate()
        

    def retranslateUi(self, PythonCalendar):
        _translate = QtCore.QCoreApplication.translate
        PythonCalendar.setWindowTitle(_translate("PythonCalendar", "MainWindow"))
        self.eventOutput.setText(_translate("PythonCalendar", "No Events This Month"))
        self.userName.setText(_translate("PythonCalendar", "User"))
        self.userTitle.setText(_translate("PythonCalendar", "User:"))
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


    def openEventWindow(self):
        self.eventWindow = QtWidgets.QMainWindow()
        self.eventUi = Ui_EventMaker()
        self.eventUi.setupUi(self.eventWindow)
        self.eventUi.createButton.clicked.connect(self.eventAddToCalendar)
        self.eventWindow.show()

    def eventAddToCalendar(self):
        event_name = self.eventUi.eventName.text()
        start_date = self.eventUi.dateTimeEditStart.dateTime().toPyDateTime()

    # Store the event in the event list as a tuple
        self.eventList.append((event_name, start_date))
    
    # Update the eventOutput label
        self.eventOutput.setText("\n".join([f"{e[0]} on {e[1].strftime('%Y-%m-%d')}" for e in self.eventList]))

        self.monthEventUpdate()

    # Highlight the day in the calendar
        highlightDay = QtGui.QTextCharFormat()
        highlightDay.setBackground(QtGui.QBrush(QtGui.QColor("yellow")))
        self.calendar_1.setDateTextFormat(start_date.date(), highlightDay)

    # Close the event window
        self.eventWindow.close()

    def monthEventUpdate(self):
        current_month = self.calendar_1.monthShown()
        current_year = self.calendar_1.yearShown()
    
    # Filter events based on the current visible month and year
        events_in_month = [
            f"{event_name} on {event_date.strftime('%Y-%m-%d')}"
            for event_name, event_date in self.eventList
            if event_date.month == current_month and event_date.year == current_year
        ]
    
    # Update the eventOutput label
        if events_in_month:
            self.eventOutput.setText("\n".join(events_in_month))
        else:
            self.eventOutput.setText("No Events This Month")
  #Highlights events 
    def highlightEvent(self, date):
        highlight = QtGui.QTextCharFormat()
        highlight.setBackground(QtGui.QBrush(QtGui.QColor("red")))
        self.calendar_1.setDateTextFormat(date, highlight)
#delets previous events
    def deletePastEvents(self):
        current_date = QtCore.QDate.currentDate()
        self.eventList = [event for event in self.eventList if event[1].date() >= current_date]
        
        self.monthEventUpdate()
        self.calendar_1.clearDateTextFormats()
        
        for event_name, event_date in self.eventList:
            if event_date.date() >= current_date:
                self.highlightEvent(event_date.date())
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PythonCalendar = QtWidgets.QMainWindow()
    ui = Ui_PythonCalendar()
    ui.setupUi(PythonCalendar)
    PythonCalendar.show()
    sys.exit(app.exec_())


