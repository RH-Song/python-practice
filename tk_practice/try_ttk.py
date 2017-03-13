import ttk

window = ttk.Tkinter.Tk()
window.title('my window')
window.geometry('200x100')

b = ttk.Button(window,text='try')
b.pack()

window.mainloop()
