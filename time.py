import time
from tkinter import messagebox
from tkinter import *


root = Tk()
root.geometry("300x200")
root.title("Time Counter")

hour = StringVar()
minute = StringVar()
second = StringVar()

hour.set("00")
minute.set("00")
second.set("00")


hourEntry = Entry(root, width = 3, font = ("Arail",15,""),textvariable=hour)
hourEntry.place(x=80,y=20)

minuteEntry = Entry(root, width = 3, font = ("Arail",15,""),textvariable=minute)
minuteEntry.place(x=130,y=20)


secondEntry = Entry(root, width = 3, font = ("Arail",15,""),textvariable=second)
secondEntry.place(x=180,y=20)

def submit():
    try:
            temp = int(hour.get())**3600 + int(minute.get())*60 + int(second.get())
    except:
        print("Please Gve Right Input")
    while temp > -1:
            mins, secs = divmod(temp, 60)
            hours = 0
            if mins >= 60:
                hours, mins = divmod(mins, 60)

            hour.set("{0:2d}".format(hours))
            minute.set("{0:2d}".format(mins))
            second.set("{0:2d}".format(secs))

            root.update()

            time.sleep(1)
            if (temp==0):
                messagebox.showinfo("Time Counter","It's Over")
            temp = temp -1




btn = Button(root, font=("Arail",10,""),text="Set Time Counter",command=submit)
btn.place(x=90,y=80)
root.mainloop()