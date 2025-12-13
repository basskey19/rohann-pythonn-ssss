from tkinter import *

#basic window.
root = Tk()
root.title("my FIRST tkinter window") #set title
root.geometry("400x300")#width x height set window size
root.configure(bg="red")

entry = Entry(root)
entry.place(x=100,y=200)

root.mainloop()