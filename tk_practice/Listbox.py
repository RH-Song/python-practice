import Tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('300x300')

var = tk.StringVar()
l = tk.Label(window,textvariable=var,bg='yellow',width=15)
l.pack()

def print_selection():
    value = lb.get(lb.curselection())
    var.set(value)

b1 = tk.Button(window,text='print selection',width=15,height=2
        ,command=print_selection)
b1.pack()

var2 = tk.StringVar()
var2.set((1,2,3,4))
lb = tk.Listbox(window,listvariable=var2)
list_items = [1,2,3,4]
for item in list_items:
    lb.insert('end',item)

lb.insert(1,'first')
lb.delete(2)

lb.pack()

window.mainloop()
