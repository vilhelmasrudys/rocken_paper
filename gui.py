from ctypes import resize
from tkinter import *
from PIL import ImageTk, Image
from matplotlib import image

#main window and an icon
root = Tk()
root.title("Rock Paper Scissors!")
root.iconbitmap('my_images/favicon.ico')
root.geometry("720x512")

#my buttons, can't find a solution on how to make them transparent
btn1 = PhotoImage(file='my_images/but1.png')
btn2 = PhotoImage(file='my_images/but2.png')
btn3 = PhotoImage(file='my_images/but3.png')

#impotring title and background images
my_title = Image.open("my_images/title.png")
resize_my_title = my_title.resize((386, 30))
title = ImageTk.PhotoImage(resize_my_title)

background = Image.open("my_images/bg.png")
resize_background = background.resize((720, 512))
bg = ImageTk.PhotoImage(resize_background)

#making a canvas, putting title and background images to work
my_canvas = Canvas(root, width=720, height=512)
my_canvas.pack(fill="both", expand=True)

my_canvas.create_image(0, 0, image=bg, anchor="nw")
my_canvas.create_image(167, 48, image=title, anchor="nw")

button1 = Button(my_canvas, image=btn1, borderwidth=0, bg="red")
button2 = Button(my_canvas, image=btn2, borderwidth=0, bg='red')
button3 = Button(my_canvas, image=btn3, borderwidth=0, bg='red')

 

button1.place(x=100, y=400)
button2.place(x=280, y=400)
button3.place(x=460, y=400)

# my_label = Label(root, image=bg)
# my_label.place(x=0, y=0, relwidth=1, relheight=1)

# my_text = Label(root, text="Welcome", font=("Helvetica", 50), fg="white")
# my_text.pack(pady=50)






root.mainloop()