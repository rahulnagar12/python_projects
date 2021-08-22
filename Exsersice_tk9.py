from tkinter import *

root = Tk()
root.title()
root.geometry("600x1000")

# function which will print data on form live
def show():
    Label(root, text = nam1.get()).grid(row=12, column=1)
    Label(root, text = nam1.get()).grid(row=13, column=1)
    Label(root, text = nam1.get()).grid(row=14, column=1)
    Label(root, text = nam1.get()).grid(row=15, column=1)
    Label(root, text = nam1.get()).grid(row=16, column=1)
    Label(root, text = nam1.get()).grid(row=17, column=1)
    Label(root, text = nam1.get()).grid(row=18, column=1)

clg_name = Label(root, text ="Govt. Pollytechnic JHALAWAR" ,
font=("arial", 20, "bold"), ).grid(columnspan = 5, row = 0, column = 1, pady = 40)


# my variables to stor values
nam1 = StringVar()
fatherval = StringVar()
motherval = StringVar()
castval = StringVar()
mobval = IntVar()
genval = StringVar()
payval = StringVar()


# names that print on form
name = Label(root, text = "NAME    -").grid(row=1, column=0, pady=5)
fa = Label(root, text = "FATHER   -").grid(row=2, column=0)
mo = Label(root, text = "MOTHER   -").grid(row=3, column=0, pady =5)
ca = Label(root, text = "CAST      -").grid(row=4, column=0, pady =5)
mob = Label(root, text = "MOBILE   -").grid(row=5, column=0, pady =5)
gender = Label(root, text = "GENDER   -").grid(row=6, column=0, pady =5)
payment = Label(root, text = "PAYMENT   -").grid(row=7, column=0, pady =5)


# Entry boxes in which user can write
namentry = Entry(root, textvariable = nam1, ).grid(row=1, column=1)
faentry = Entry(root, textvariable = fatherval, ).grid(row=2, column=1)
momentry = Entry(root, textvariable=motherval, ).grid(row=3, column=1)
camentry = Entry(root, textvariable=castval, ).grid(row=4, column=1)
mobmentry = Entry(root, textvariable=mobval, ).grid(row=5, column=1)


# check buttons and radio buttons for form

genbtn = Radiobutton(text = "MALE", variable= genval, value = "Male")
genbtn.deselect()
genbtn.grid(row=6, column=1)
genbtn1 = Radiobutton(text = "FEMALE", variable= genval, value = "Female")
genbtn1.deselect()
genbtn1.grid(row=6, column=2)


paybtn = Checkbutton(text="CASH ", variable = payval, onvalue="CASH", offvalue="None")
paybtn.deselect()
paybtn.grid(row=7, column=1)
paybtn1 = Checkbutton(text="DIGITAL ", variable = payval, onvalue="DIGITAL", offvalue="None")
paybtn1.deselect()
paybtn1.grid(row=7, column=2)

# Sumbmit btn and print btn for form

prn = Button(root, text = "SHOW", COMMAND=show)



root.mainloop()