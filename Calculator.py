import tkinter as tk
root = tk.Tk()
e = tk.Entry(root, width=35, borderwidth=5)
e.grid(row=0,columnspan=3,padx=10,pady=10)
def button_click(number):
    current = e.get()
    e.delete(0,tk.END)
    e.insert(0,str(current)+str(number))
def button_clear():
    e.delete(0, tk.END)
def button_add():
    first = e.get()
    global firstn
    global cal
    cal = "addition"
    firstn = int(first)
    e.delete(0, tk.END)
def button_subtract():
    first = e.get()
    global firstn
    global cal
    cal = "subtraction"
    firstn = int(first)
    e.delete(0, tk.END)
def button_equal():
    second = e.get()
    e.delete(0, tk.END)
    if cal=="addition":
        e.insert(0,firstn+int(second))
    elif cal=="subtraction":
        e.insert(0,firstn-int(second))


button_1 = tk.Button(root, text="1", padx=40, pady=20, command=lambda:button_click(1))
button_2 = tk.Button(root, text="2", padx=40, pady=20, command=lambda:button_click(2))
button_3 = tk.Button(root, text="3", padx=40, pady=20, command=lambda:button_click(3))
button_4 = tk.Button(root, text="4", padx=40, pady=20, command=lambda:button_click(4))
button_5 = tk.Button(root, text="5", padx=40, pady=20, command=lambda:button_click(5))
button_6 = tk.Button(root, text="6", padx=40, pady=20, command=lambda:button_click(6))
button_7 = tk.Button(root, text="7", padx=40, pady=20, command=lambda:button_click(7))
button_8 = tk.Button(root, text="8", padx=40, pady=20, command=lambda:button_click(8))
button_9 = tk.Button(root, text="9", padx=40, pady=20, command=lambda:button_click(9))
button_0 = tk.Button(root, text="0", padx=40, pady=20, command=lambda:button_click(0))
button_add = tk.Button(root, text="+", padx=40, pady=20, command=button_add)
button_subtract = tk.Button(root, text="-", padx=40, pady=20, command=button_subtract)
button_equal = tk.Button(root, text="=", padx=40, pady=20, command=button_equal)
button_clear = tk.Button(root, text="clear", padx=120, pady=20, command=button_clear)
button_1.grid(row=1,column=0)
button_2.grid(row=1,column=1)
button_3.grid(row=1,column=2)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)

button_7.grid(row=3,column=0)
button_8.grid(row=3,column=1)
button_9.grid(row=3,column=2)

button_0.grid(row=4,column=0)
button_add.grid(row=1,column=3)
button_subtract.grid(row=2,column=3)
button_equal.grid(row=3,column=3)
button_clear.grid(row=4,column=1,columnspan=3)
root.mainloop()