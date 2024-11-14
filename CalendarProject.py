
#We relied heavily on PyQt5 and Designer in our beta UI development
import pickle #Pickle is being used for our open functions
from PyQt5 import QtCore, QtGui, QtWidgets
from EventCreation import Ui_EventMaker
from EventDeletion import Ui_DeleteEvent
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PythonCalendar(object):
    #The UI is set up with the below code
    def setupUi(self, PythonCalendar, username = "User"):
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

        self.actionAdd.triggered.connect(self.openEventWindow)
        self.eventList = []
        self.calendar_1.currentPageChanged.connect(self.monthEventUpdate)
        self.monthEventUpdate()
        self.actionDelete.triggered.connect(self.openDeleteWindow)
        self.actionSave.triggered.connect(self.saveCalendar)
        self.actionOpenFile.triggered.connect(self.loadCalendar)

    def retranslateUi(self, PythonCalendar):
        _translate = QtCore.QCoreApplication.translate
        PythonCalendar.setWindowTitle(_translate("PythonCalendar", "Python Calendar"))
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
        self.actionOpenFile.setText(_translate("PythonCalendar", "Open"))


    def openEventWindow(self): #Opens Event Window
        self.eventWindow = QtWidgets.QMainWindow()
        self.eventUi = Ui_EventMaker()
        self.eventUi.setupUi(self.eventWindow) #UI Setup
        self.eventUi.createButton.clicked.connect(self.eventAddToCalendar)
        self.eventWindow.show()

    def eventAddToCalendar(self):
        event_name = self.eventUi.eventName.text() #Adds eventname
        start_date = self.eventUi.dateTimeEditStart.dateTime().toPyDateTime()
        
    #Store the event in the event list as a tuple
        self.eventList.append((event_name, start_date))
    
    #Update the eventOutput label
        self.eventOutput.setText("\n".join([f"{e[0]} on {e[1].strftime('%Y-%m-%d')}" for e in self.eventList]))

        self.monthEventUpdate()

    #Highlight the day in the calendar
        highlightDay = QtGui.QTextCharFormat()
        highlightDay.setBackground(QtGui.QBrush(QtGui.QColor("light blue")))
        self.calendar_1.setDateTextFormat(start_date.date(), highlightDay)

    #Close the event window
        self.eventWindow.close()

    def monthEventUpdate(self):
        current_month = self.calendar_1.monthShown()
        current_year = self.calendar_1.yearShown()
    
    #Filter events based on the current visible month and year
        events_in_month = [
            f"{event_name} on {event_date.strftime('%Y-%m-%d')}"
            for event_name, event_date in self.eventList
            if event_date.month == current_month and event_date.year == current_year
        ] #Only prints the events and updates on their effective month
    
    #Update the eventOutput label
        if events_in_month:
            self.eventOutput.setText("\n".join(events_in_month))
        else:
            self.eventOutput.setText("No Events This Month")
    #Highlights events 
    def highlightEvent(self, date):
        highlight = QtGui.QTextCharFormat()
        highlight.setBackground(QtGui.QBrush(QtGui.QColor("light blue")))
        self.calendar_1.setDateTextFormat(date, highlight)
    #delets previous events
    def deletePastEvents(self):
        current_date = QtCore.QDate.currentDate()
        self.eventList = [event for event in self.eventList if event[1].date() >= current_date]
        
        self.monthEventUpdate()
        self.calendar_1.clearDateTextFormats() #Clear data
        
        for event_name, event_date in self.eventList:
            if event_date.date() >= current_date:
                self.highlightEvent(event_date.date())

    def openDeleteWindow(self):
        #Delete window is opened and the events are populated
        self.deleteWindow = QtWidgets.QMainWindow()
        self.deleteUi = Ui_DeleteEvent()
        self.deleteUi.setupUi(self.deleteWindow)
        self.deleteUi.comboBox.clear()

        #Adds the events to the dropdown window
        for event_name, event_date in self.eventList:
            event_id = f"{event_name} on {event_date.strftime('%Y-%m-%d')}"  # Include the date
            self.deleteUi.comboBox.addItem(event_id)

        #Delete button function is connected
        self.deleteUi.deleteButton.clicked.connect(self.deleteEvent)
        self.deleteWindow.show()  #Opens window


    def deleteEvent(self):
        event_text = self.deleteUi.comboBox.currentText()  #Grabs event text

        removableEvent = None
        #Removes from list/combo box
        for event in self.eventList:
            event_name, event_date = event
            event_textBox = f"{event_name} on {event_date.strftime('%Y-%m-%d')}"

            if event_textBox == event_text:
                removableEvent = event
                break  

        
        if removableEvent:
            self.eventList.remove(removableEvent)
        #Default format will remove highlights from the calendar
    
        default = QtGui.QTextCharFormat() 
        default.setBackground(QtGui.QBrush(QtGui.QColor("white")))  # Set background to transparent
        self.calendar_1.setDateTextFormat(removableEvent[1].date(), default)


        #Re-highlight remaining events
        for _, event_date in self.eventList:
            self.highlightEvent(event_date.date())

        self.monthEventUpdate()
        self.deleteWindow.close()


    def saveCalendar(self):
       #Calendar save functionality
        options = QtWidgets.QFileDialog.Options()
        file_path, _ = QtWidgets.QFileDialog.getSaveFileName(None, "Save Calendar", "", "Pickle Files (*.pkl)", options=options)
        
        if file_path:
            #Save the username and event list to a file
            with open(file_path, 'wb') as file:
                pickle.dump({'username': self.userName.text(), 'events': self.eventList}, file)
            QtWidgets.QMessageBox.information(None, "Save File", "Calendar Saved")

    def loadCalendar(self):
        #Load Calendar should load pickle files
        options = QtWidgets.QFileDialog.Options()
        file_path, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Load Calendar", "", "Pickle Files (*.pkl)", options=options)

        if file_path:
            #Load the data and set it to the calendar
            with open(file_path, 'rb') as file:
                data = pickle.load(file)
                self.userName.setText(data['username'])
                self.eventList = data['events']

            #Update display with loaded events
            self.monthEventUpdate()
            self.calendar_1.clearDateTextFormats()  #Clear previous highlights

            #Re-highlight loaded events
            for _, event_date in self.eventList:
                self.highlightEvent(event_date.date())
            QtWidgets.QMessageBox.information(None, "Load", "Calendar loaded successfully!")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PythonCalendar = QtWidgets.QMainWindow()
    ui = Ui_PythonCalendar()
    ui.setupUi(PythonCalendar)
    PythonCalendar.show()
    sys.exit(app.exec_())
