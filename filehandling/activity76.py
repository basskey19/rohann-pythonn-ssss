from tkinter import *
root = Tk()
root.title("Grid ex")

def hello():
    print("hello ur form has been sumbitted")

Label1 = Label(root,text="USER ID:")
Label1.grid(row=0,column=0,padx=5,pady=5)

entry1 = Entry(root)
entry1.grid(row=0,column=1,padx=5,pady=5)

label2 = Label(root,text="Password:")
label2.grid(row=1,column=0,padx=5,pady=5)

entry2 = Entry(root,show="*")
entry2.grid(row=1,column=1,padx=5,pady=5)

button = Button(root,text="Login",command=hello)
button.grid(row=2,column=0,padx=2,pady=10)

root.mainloop()