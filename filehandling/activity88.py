from tkinter import*
from tkinter import messagebox
from PIL import Image, ImageTk 

root = Tk()
root.title("Tkinter Basics")
root.geometry("400x400")

def show_image():
    imgwindow = Toplevel(root)
    imgwindow.title("Image window")

    img = Image.open("nemo.jpg")
    img = img.resize((200,200))
    img_tk = ImageTk.Photoimage(img)

    img_label = Label(imgwindow,image = img_tk)
    img_label.image = img_tk
    img_label.pack()#used to make things in center

def show_message():
    messagebox.showinfo("YOUR Message", "Hello Alies")

def open_top_window():
    top = Toplevel(root)
    top.title("top window")
    top.geometry("250x150")
    Label(top,text = "New top window ",font=("Arial",12)).pack(pady=20)

btn1 = Button(root,text = "show Image",command=show_image)
btn1.pack(pady = 10)

btn2 = Button(root,text = "show message box",command=show_message)
btn2.pack(pady=10) 

btn3 = Button(root,text = "open top window",command=open_top_window)
btn3.pack(pady=10)
 
root.mainloop() 