from tkinter import *

from pkg_resources import EntryPoint
root=Tk()

user=Label(root,text="Username",padx=50,pady=50)
password=Label(root,text="Password",padx=50,pady=50)

user.grid(row=0)
password.grid(row=1)

uservalue=StringVar()
passvalue=StringVar()

userentry=Entry(root,textvariable=uservalue)
passentry=Entry(root,textvariable=passvalue)

userentry.grid(row=0,column=1)
passentry.grid(row=1,column=1)
root.mainloop()
