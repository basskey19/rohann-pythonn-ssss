from tkinter import *
root = Tk()
root.title("Twinkle basics")
root.geometry("300x200")

def data():
    print("Data sumbitted")

Label1 = Label(root,text="Welcome to TKInter!!!!",font=("Arial",12))
entry = Entry(root,width=20)
button = Button(root,text="sumbit",command=data)

Label1.grid(row=0,column=0,columnspan=2,pady=5)
entry.grid(row=1,column=0,columnspan=5,pady=5)
button.grid(row=1,column=1,columnspan=5,pady=5)

root.mainloop()