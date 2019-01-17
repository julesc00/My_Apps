from tkinter import *

"""Mass Converter from kilos to pounds and ounces."""

window = Tk()
window.title('Convertidor de Masas')

def kg_to_pounds():
    pounds = float(e1_value.get()) * 2.20462
    ounces = float(e1_value.get()) * 35.274
    t1.delete("1.0", END) # Erases the last result to display the new one.
    t1.insert(END, pounds)
    t2.delete("1.0", END)
    t2.insert(END, ounces)

label1 = Label(window, text="Cantidad Kg:")
label1.grid(row=0, column=0)

label2 = Label(window, text="Libras:")
label2.grid(row=1, column=0)
label3 = Label(window, text="Onzas:")
label3.grid(row=2, column=0)

label4 = Label(window, text="por: Julio")
label4.grid(row=2, column=3)

b1 = Button(window, text="Convertir", command=kg_to_pounds)
b1.grid(row=0, column=3)

b2 = Button(window, text="Salir", command=window.destroy)
b2.grid(row=1, column=3)

e1_value = StringVar()
e1 = Entry(window, textvariable=e1_value)
e1.grid(row=0, column=1)

t1 = Text(window, height=1, width=20)
t1.grid(row=1, column=1)

t2 = Text(window, height=1, width=20)
t2.grid(row=2, column=1)

window.mainloop()
