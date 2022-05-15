import tkinter as tk
from functools import partial
from correo_ventana2 import ventana2


master=tk.Tk()
master.title("Automatas finitos")




"""---------BOTONES-----------------------------------------"""
button1=tk.Button(master,command=ventana2, text="Correo Electronico")
button1.grid(row=1,column=0)

button2=tk.Button(master, text="Télefono")
button2.grid(row=2,column=0)

button3=tk.Button(master, text="Fechas(dd/mm/aaaa)")
button3.grid(row=3)

button4=tk.Button(master, text="Horas(hh:mm)")
button4.grid(row=4)

button5=tk.Button(master, text="Dirección WEB")
button5.grid(row=5)

button6=tk.Button(master, text="Dirección IP")
button6.grid(row=6)

button7=tk.Button(master, text="Folio Fiscal")
button7.grid(row=7)

button8=tk.Button(master, text="RFC")
button8.grid(row=8)

button9=tk.Button(master, text="CURP")
button9.grid(row=9)


master.mainloop()