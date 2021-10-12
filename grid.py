from tkinter import *
root = Tk()
# Creating a lable
Mylable = Label(root, text="Hello Python GUI\nAbtin Zandi")
Mylable2 = Label(root, text = "Iran,Tehran,19")
Mylable2.grid(row=2, column=2)
Mylable.grid(row=0,column=0)
root.mainloop()