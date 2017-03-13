import Tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('300x300')

l = tk.Label(window,bg='blue',width=20,text='I don\'t love either')
l.pack()

def print_selection():
    if(var1.get() == 1) & (var2.get() == 1):
        l.config(text='I love both')
    elif(var1.get() == 1) & (var2.get() == 0):
        l.config(text='I love only Python')
    elif(var1.get() == 0) & (var2.get() == 1):
        l.config(text='I love only C++')
    else :
        l.config(text='I don\'t love either')

var1 = tk.IntVar()
var1.set(0)
c1 = tk.Checkbutton(window,text='Python',variable=var1,onvalue='1',
        offvalue='0',command=print_selection)
c1.pack()

var2 = tk.IntVar()
var2.set(0)
c2 = tk.Checkbutton(window,text='C++',variable=var2,onvalue='1',
        offvalue='0',command=print_selection)
c2.pack()

window.mainloop()
