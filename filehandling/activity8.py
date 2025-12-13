from tkinter import*
from tkinter import messagebox

root = Tk()
root.title("First apperance")
root.geometry("200x200")

def msg():

    messagebox.showinfo("Welcome","By opening this window u have a chance of 99.9 chance of getting a virus")
    messagebox.showwarning("ALERT","Fortunately u got Sonic.Exe")

button = Button(root,text="scanning for virus",command=msg)
button.place(x=40,y=80)

root.mainloop()