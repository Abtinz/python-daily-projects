from tkinter import *
root = Tk()

###first step
#london = Button(root, text="london")
#london.grid(row=2, column=2)
### x and y expadtion
#canada = Button(root,text="CANADA",padx=50,pady=50)
#canada.grid(row=3, column=2)
###calclatorrrrrrr
cal1= Button(root,text="1",padx=50,pady=50)
cal2= Button(root,text="2",padx=50,pady=50)
cal3= Button(root,text="3",padx=50,pady=50)
cal4= Button(root,text="4",padx=50,pady=50)
cal5= Button(root,text="5",padx=50,pady=50)
cal6= Button(root,text="6",padx=50,pady=50)
cal7= Button(root,text="7",padx=50,pady=50)
cal8= Button(root,text="8",padx=50,pady=50)
cal0= Button(root,text="0",padx=50,pady=50)
cal9= Button(root,text="9",padx=50,pady=50)
calHash= Button(root,text="#",padx=50,pady=50)
calStr= Button(root,text="*",padx=50,pady=50)

cal1.grid(row=0, column=0)
cal2.grid(row=0, column=1)
cal3.grid(row=0, column=2)
cal4.grid(row=1, column=0)
cal5.grid(row=1, column=1)
cal6.grid(row=1, column=2)
cal7.grid(row=2, column=0)
cal8.grid(row=2, column=1)
cal9.grid(row=2, column=2)
calHash.grid(row=3, column=0)
cal0.grid(row=3, column=1)
calStr.grid(row=3, column=2)
root.mainloop()