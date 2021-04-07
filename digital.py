# The libraries used are Tkinter and Time
from tkinter import Label,Tk
from time import strftime


#======= Configuring window =========
window = Tk()
window.title("")
window.geometry("200x150")
window.configure(bg="orange")

clock_label = Label(window, bg="maroon", fg="white", font = ("Times", 30), relief='flat')
clock_label.place(x = 20, y = 20)

def update_label():
    current_time = strftime('%H: %M: %S')
    clock_label.configure(text = current_time)
    clock_label.after(80, update_label)

update_label()
window.mainloop()
