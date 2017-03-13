import Tkinter as tk
import time
import threading

if __name__=='__main__':
    
    window = tk.Tk()
    window.title('my window')
    window.geometry('300x300')
    
    l = tk.Label(window, bg='yellow',width=20,text='empty')
    l.pack()
    
    def print_selection(v):
        l.config(text='You have select ' + v)
    
    svalue = 0
    s = tk.Scale(window,label='try',from_=0,to=11,orient=tk.HORIZONTAL,
            length=200,tickinterval=2,resolution=0.01,
            command=print_selection)
    s.pack()
    for i in range(12):
        s.set(i)
        time.sleep(1)
    
    window.mainloop()
