#Calendar App
import tkinter as tk
from tkcalendar import Calendar

def main():

    application = tk.Tk()
    application.title("Calendar Test")
    calendar = Calendar(application)
    calendar.pack(padx = 15, pady = 15)
    application.mainloop

main()