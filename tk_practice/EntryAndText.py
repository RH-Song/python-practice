import Tkinter as tk

window = tk.Tk()

window.title('my window')
window.geometry('200x200')

e = tk.Entry(window,show='*')
e.pack()

def insert_point():
    var = e.get()
    global insert_point_button
    insert_point_bg = 'green'
    insert_point_button.configure(bg=insert_point_bg)
    t.insert('insert',var)
    
insert_point_bg = 'red'
insert_point_button = tk.Button(window, text='insert point',width=15,
        height=2,command=insert_point,bg=insert_point_bg)

insert_point_button.pack()

def insert_end():
    var = e.get()
    t.insert('end',var)

insert_end_button = tk.Button(window, text='insert end',width=15,
        height=2,command=insert_end)

insert_end_button.pack()


t = tk.Text(window,height=2)
t.pack()

window.mainloop()
