from tkinter import * 

root = Tk()
root.geometry('500x500')
root.title("Registration Form")

Label(root, text="Registration form",width=20,font=("bold", 20)).place(x=90,y=53)


Label(root, text="FullName",width=20,font=("bold", 10)).place(x=80,y=130)

Entry(root).place(x=240,y=130)


Label(root, text="Gender",width=20,font=("bold", 10)).place(x=70,y=230)
var = IntVar()
Radiobutton(root, text="Male",padx = 5, variable=var, value=1).place(x=235,y=230)
Radiobutton(root, text="Female",padx = 20, variable=var, value=2).place(x=290,y=230)




Button(root, text='Submit',width=20,bg='brown',fg='white').place(x=180,y=380)

root.mainloop()