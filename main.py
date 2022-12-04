from tkinter import *

window = Tk()
window.title("Mile to Km convertor")
window.minsize(450, 450)
window.config(padx=30, pady=30)

mile_entrty = Entry(width=20)
mile_entrty.grid(column=0, row=0)

lable1 = Label(text="Miles is equal to", font=("lalezar", 15))
lable1.grid(column=1, row=0)
lable1.config(padx=10, pady=10)

kilometer_label = Label(text="0", font=("lalezar", 15))
kilometer_label.grid(column=2, row=0)

lable2 = Label(text="km", font=("lalezar", 15))
lable2.grid(column=3, row=0)
lable2.config(padx=10)


def convert():

    mile = float(mile_entrty.get())
    kilometer = mile * 1.6
    kilometer_label.config(text=kilometer)


button = Button(text="Convert", command=convert)
button.grid(column=1, row=1)

window.mainloop()
