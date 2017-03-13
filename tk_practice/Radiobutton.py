import Tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('300x300')

var = tk.StringVar()
l = tk.Label(window,bg='yellow',textvariable=var,width=15)
l.pack()

def print_selection():
    t.insert('end','It works')

r1 = tk.Radiobutton(window,text='A',variable=var,value='A',
        command=print_selection)
r1.pack()

r2 = tk.Radiobutton(window,text='B',variable=var,value='B',
        command=print_selection)
r2.pack()

r3 = tk.Radiobutton(window,text='C',variable=var,value='C',
        command=print_selection)
r3.pack()

t = tk.Text(window,height=2)
t.pack()

window.mainloop()
