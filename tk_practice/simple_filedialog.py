import Tkinter as tk
import tkFileDialog as filedialog
#import filedialog

root = tk.Tk()
root.title('MyGod')
root.geometry('500x100')

path = tk.StringVar()

entry = tk.Entry(root,bg='gray',textvariable=path,width=50)
entry.pack()
def select_file():
    entry.delete(0,tk.END)
    filepath = filedialog.askopenfilename(filetypes=(('all files','*.*'),
        ('pcap files','*.pcap')))
    if filepath:
        entry.insert(0,filepath)

b = tk.Button(root,text='select file',bg='green',command=select_file)
b.pack()

root.mainloop()
