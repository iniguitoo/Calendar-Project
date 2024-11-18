#We relied heavily on PyQt5 and Designer in our beta UI development
import pickle #Pickle is being used for our open functions
from PyQt5 import QtCore, QtGui, QtWidgets
from EventCreation import Ui_EventMaker
from EventDeletion import Ui_DeleteEvent
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QFontDatabase 


class Ui_PythonCalendar(object):
    #The UI is set up with the below code
    def __init__(self):
        regular_font_id = QFontDatabase.addApplicationFont("fonts/ProductSans-Regular.ttf")
        if regular_font_id == -1:
            print("Failed to load Product Sans Regular font.")
        else:
            self.product_sans_regular = QFontDatabase.applicationFontFamilies(regular_font_id)[0]

    def setupUi(self, PythonCalendar, username="User"):
        PythonCalendar.setObjectName("PythonCalendar")
        PythonCalendar.resize(904, 859)
        self.centralwidget = QtWidgets.QWidget(PythonCalendar)
        self.centralwidget.setObjectName("centralwidget")

        # Set up the layout for central widget to allow resizing
        main_layout = QtWidgets.QVBoxLayout(self.centralwidget)

        # Calendar widget setup with custom font
        self.calendar_1 = QtWidgets.QCalendarWidget(self.centralwidget)
        calendar_font = QtGui.QFont(self.product_sans_regular, 10)  # Adjust size as needed
        self.calendar_1.setFont(calendar_font)
        self.calendar_1.setObjectName("calendar_1")
        self.calendar_1.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)

        # Event Output label with custom font
        self.eventOutput = QtWidgets.QLabel(self.centralwidget)
        event_font = QtGui.QFont(self.product_sans_regular, 14)
        self.eventOutput.setFont(event_font)
        self.eventOutput.setAlignment(QtCore.Qt.AlignCenter)
        self.eventOutput.setObjectName("eventOutput")

        # User title
        self.userTitle = QtWidgets.QLabel(self.centralwidget)
        title_font = QtGui.QFont(self.product_sans_regular, 14)
        self.userTitle.setFont(title_font)
        self.userTitle.setObjectName("userTitle")
        
        # User name
        self.userName = QtWidgets.QLabel(self.centralwidget)
        name_font = QtGui.QFont(self.product_sans_regular, 14)
        self.userName.setFont(name_font)
        self.userName.setObjectName("userName")

        # Adding widgets to the layout
        top_layout = QtWidgets.QHBoxLayout()
        top_layout.addStretch(1)
        top_layout.addWidget(self.userTitle)
        top_layout.addSpacing(5)  
        top_layout.addWidget(self.userName)
        top_layout.setContentsMargins(0, 10, 20, 10)  
        
        # Update the main layout
        main_layout.addLayout(top_layout)  # Add the top row
        main_layout.addWidget(self.calendar_1)  # Add calendar
        main_layout.addWidget(self.eventOutput)  # Add event output

        PythonCalendar.setCentralWidget(self.centralwidget)

        # Set custom font for the entire calendar widget's internal elements
        calendar_font_smaller = QtGui.QFont(self.product_sans_regular, 9)  # Smaller font for calendar elements
        self.calendar_1.setStyleSheet(f"""
            QCalendarWidget QToolButton {{
                font-family: {self.product_sans_regular};
                font-size: 9pt;
            }}
            QCalendarWidget QSpinBox {{
                font-family: {self.product_sans_regular};
                font-size: 9pt;
            }}
            QCalendarWidget QTableView {{
                font-family: {self.product_sans_regular};
                font-size: 9pt;
            }}
        """)

        self.menubar = QtWidgets.QMenuBar(PythonCalendar)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 904, 21))
        self.menubar.setObjectName("menubar")
        
        # Set font for menu bar
        menu_font = QtGui.QFont(self.product_sans_regular, 9)
        self.menubar.setFont(menu_font)
        self.menufile = QtWidgets.QMenu(self.menubar)
        self.menufile.setObjectName("menufile")
        self.menuShare = QtWidgets.QMenu(self.menufile)
        self.menuShare.setObjectName("menuShare")
        self.menuNew = QtWidgets.QMenu(self.menufile)
        self.menuNew.setObjectName("menuNew")
        self.menuEvent = QtWidgets.QMenu(self.menubar)
        self.menuEvent.setObjectName("menuEvent")
        PythonCalendar.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(PythonCalendar)
        self.statusbar.setObjectName("statusbar")
        PythonCalendar.setStatusBar(self.statusbar)

        # Other actions for menu bar
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
        self.menuEvent.addAction(self.actionAdd)
        self.menuEvent.addAction(self.actionDelete)
        self.menuEvent.addSeparator()
        self.menubar.addAction(self.menufile.menuAction())
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
        self.userTitle.setText(_translate("PythonCalendar", "User:"))
        self.userName.setText(_translate("PythonCalendar", "User"))
        self.menufile.setTitle(_translate("PythonCalendar", "File"))
        self.menuShare.setTitle(_translate("PythonCalendar", "Share"))
        self.menuNew.setTitle(_translate("PythonCalendar", "New"))
    
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

    def highlightDateRange(self, start_date, end_date):
        """Helper function to highlight a range of dates"""
        highlightDay = QtGui.QTextCharFormat()
        highlightDay.setBackground(QtGui.QBrush(QtGui.QColor("light blue")))
        
        # Convert datetime objects to QDate
        start_qdate = QtCore.QDate(start_date.year, start_date.month, start_date.day)
        end_qdate = QtCore.QDate(end_date.year, end_date.month, end_date.day)
        
        # Highlight each day in the range
        current_date = start_qdate
        while current_date <= end_qdate:
            self.calendar_1.setDateTextFormat(current_date, highlightDay)
            current_date = current_date.addDays(1)

    def clearAllHighlights(self):
        """Helper function to clear all highlights from the calendar"""
        default = QtGui.QTextCharFormat()
        default.setBackground(QtGui.QBrush(QtGui.QColor("white")))
        
        # Get the first day of the current month
        current_month = self.calendar_1.monthShown()
        current_year = self.calendar_1.yearShown()
        first_day = QtCore.QDate(current_year, current_month, 1)
        
        # Get the last day of the current month
        if current_month == 12:
            next_year = current_year + 1
            next_month = 1
        else:
            next_year = current_year
            next_month = current_month + 1
        last_day = QtCore.QDate(next_year, next_month, 1).addDays(-1)
        
        # Clear highlights for the current month view only
        current_date = first_day
        while current_date <= last_day:
            self.calendar_1.setDateTextFormat(current_date, default)
            current_date = current_date.addDays(1)


    def openEventWindow(self): #Opens Event Window
        self.eventWindow = QtWidgets.QMainWindow()
        self.eventUi = Ui_EventMaker()
        self.eventUi.setupUi(self.eventWindow) #UI Setup
        self.eventUi.createButton.clicked.connect(self.eventAddToCalendar)
        self.eventWindow.show()

    def eventAddToCalendar(self):
        event_name = self.eventUi.eventName.text()
        start_date = self.eventUi.dateTimeEditStart.dateTime().toPyDateTime()
        end_date = self.eventUi.dateTimeEdit.dateTime().toPyDateTime()
        event_color = self.eventUi.selectedColor  # Get the selected color
        
        # Store the event in the event list with color
        self.eventList.append((event_name, start_date, end_date, event_color))
        
        # Update the calendar view and highlights
        self.monthEventUpdate()
        
        # Close the event window
        self.eventWindow.close()


    def monthEventUpdate(self):
        current_month = self.calendar_1.monthShown()
        current_year = self.calendar_1.yearShown()
        
        # Clear existing highlights for the current month view
        self.clearAllHighlights()
        
        # Re-highlight all events with their specific colors
        for event_name, start_date, end_date, event_color in self.eventList:
            # Check if any part of the event falls in the current month/year
            event_start = QtCore.QDate(start_date.year, start_date.month, start_date.day)
            event_end = QtCore.QDate(end_date.year, end_date.month, end_date.day)
            
            # Highlight the date range for each event with its color
            current_date = event_start
            while current_date <= event_end:
                highlight = QtGui.QTextCharFormat()
                # Use the event's color with 50% transparency
                color = QtGui.QColor(event_color)
                color.setAlpha(128)  # Set transparency
                highlight.setBackground(QtGui.QBrush(color))
                self.calendar_1.setDateTextFormat(current_date, highlight)
                current_date = current_date.addDays(1)
        
        # Filter events for display in the event output
        events_in_month = [
            f"{event_name} starts  {start_date.strftime('%Y-%m-%d')} at {start_date.strftime('%H:%M')} "
            f"and finishes {end_date.strftime('%Y-%m-%d')} {end_date.strftime('%H:%M')}"
            for event_name, start_date, end_date, _ in self.eventList
            if (start_date.month == current_month and start_date.year == current_year) or
            (end_date.month == current_month and end_date.year == current_year)
        ]
        
        # Update the eventOutput label
        if events_in_month:
            self.eventOutput.setText("\n".join(events_in_month))
        else:
            self.eventOutput.setText("No Events This Month")



    #delets previous events
    def deletePastEvents(self):
        current_date = QtCore.QDate.currentDate()
        self.eventList = [event for event in self.eventList if event[1].date() >= current_date]
        
        self.monthEventUpdate()
        self.calendar_1.clearDateTextFormat() #Clear data
        
        for event_name, event_date in self.eventList:
            if event_date.date() >= current_date:
                self.highlightEvent(event_date.date())

    def openDeleteWindow(self):
        self.deleteWindow = QtWidgets.QMainWindow()
        self.deleteUi = Ui_DeleteEvent()
        self.deleteUi.setupUi(self.deleteWindow)
        self.deleteUi.comboBox.clear()

        # Add the events to the dropdown window with new format
        # Update the unpacking to include the color
        for event_name, start_date, end_date, event_color in self.eventList:  # Changed this line
            event_id = (f"{event_name} on {start_date.strftime('%Y-%m-%d')} at {start_date.strftime('%H:%M')} "
                    f"and finishes {end_date.strftime('%Y-%m-%d')} at {end_date.strftime('%H:%M')}")
            self.deleteUi.comboBox.addItem(event_id)

        self.deleteUi.deleteButton.clicked.connect(self.deleteEvent)
        self.deleteWindow.show()


    def deleteEvent(self):
        event_text = self.deleteUi.comboBox.currentText()

        removableEvent = None
        for event in self.eventList:
            event_name, start_date, end_date, _ = event
            event_textBox = (f"{event_name} on {start_date.strftime('%Y-%m-%d')} at {start_date.strftime('%H:%M')} "
                            f"and finishes {end_date.strftime('%Y-%m-%d')} at {end_date.strftime('%H:%M')}")

            if event_textBox == event_text:
                removableEvent = event
                break

        if removableEvent:
            self.eventList.remove(removableEvent)
            self.monthEventUpdate()  # This will handle clearing and re-highlighting

        self.deleteWindow.close()


    def saveCalendar(self):
        options = QtWidgets.QFileDialog.Options()
        file_path, _ = QtWidgets.QFileDialog.getSaveFileName(None, "Save Calendar", "", "Pickle Files (*.pkl)", options=options)
        
        if file_path:
            with open(file_path, 'wb') as file:
                pickle.dump({'username': self.userName.text(), 'events': self.eventList}, file)
            QtWidgets.QMessageBox.information(None, "Save File", "Calendar Saved")

    def loadCalendar(self):
        options = QtWidgets.QFileDialog.Options()
        file_path, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Load Calendar", "", "Pickle Files (*.pkl)", options=options)

        if file_path:
            try:
                with open(file_path, 'rb') as file:
                    data = pickle.load(file)
                    
                if 'username' in data and 'events' in data:
                    self.userName.setText(data['username'])
                    # Convert old format events to new format if needed
                    self.eventList = []
                    for event in data['events']:
                        if len(event) == 3:  # Old format without color
                            name, start, end = event
                            self.eventList.append((name, start, end, "#03a9f4"))  # Default color
                        else:  # New format with color
                            self.eventList.append(event)
                            
                    self.monthEventUpdate()
                    QtWidgets.QMessageBox.information(None, "Load File", "Calendar loaded successfully!")
                else:
                    QtWidgets.QMessageBox.warning(None, "Load File", "Invalid calendar file format.")
            except Exception as ex:
                QtWidgets.QMessageBox.critical(None, "Load Error", f"Calendar Could not be loaded: {ex}")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PythonCalendar = QtWidgets.QMainWindow()
    ui = Ui_PythonCalendar()
    ui.setupUi(PythonCalendar)
    PythonCalendar.show()
    sys.exit(app.exec_())