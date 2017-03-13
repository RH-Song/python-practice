import Tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('300x300')

canvas = tk.Canvas(window,bg='green',height=200,width=300)
canvas.pack()

## Maybe here need PIL ImageTk
# image_file = tk.PhotoImage(file='sean.png')
# image = canvas.create_image(10,10,anchor='nw',image=image_file)

window.mainloop()
