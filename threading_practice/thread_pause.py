import threading
import Tkinter as tk
import time

def run():
    global pause_flag
    for i in range(10):
        print(i)
        time.sleep(1)
        while pause_flag:
            pass

def pau():
    pass

def start():
    global pause_flag
    pause_flag = False
    running = threading.Thread(target=run)
    running.start()

def pause():
    global pause_flag 
    pause_flag = ~pause_flag
    #pause = threading.Thread(target=pau)
    #pause.start()
    
def layout():
    main_window = tk.Tk()
    main_window.title('test')
    main_window.geometry('300x200')

    start_button = tk.Button(main_window,text='start',bg='green',
            command=start)
    start_button.pack()
    pause_button = tk.Button(main_window,text='pause',bg='red',
            command=pause)
    pause_button.pack()

    main_window.mainloop()
if __name__=='__main__':
    pause_flag = True
    layout_thread = threading.Thread(target=layout)
    layout_thread.start()
    layout_thread.join()
