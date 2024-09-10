#Calendar App
import tkinter as tk
from tkcalendar import Calendar



application = tk.Tk()
application.title("Calendar Test")
calendar = Calendar(
application,
selectmode = "day", 
firstweekday = 'sunday',                 
)
calendar.pack(padx = 15, pady = 15)

application.mainloop()