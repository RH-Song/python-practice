import Tkinter as tk
import pickle

window = tk.Tk()
window.title('Welcome to Sean Python Practice')
window.geometry('500x300')

canvas = tk.Canvas(window,width=500,height=200)
image_file = tk.PhotoImage(file='welcome.gif')
image = canvas.create_image(30,0,anchor='nw',image=image_file)
canvas.pack(side='top')

# labels show informatin
name_lable = tk.Label(window,text='User name:')
name_lable.place(x=50,y=150)
passwd_lable = tk.Label(window,text='Password:')
passwd_lable.place(x=50,y=190)

# Enter user information
var_usr_name = tk.StringVar()
var_usr_name.set('example@python.com')
name_entry = tk.Entry(window,width=48,textvariable=var_usr_name)
name_entry.place(x=120,y=150)

var_usr_passwd = tk.StringVar()
passwd_entry = tk.Entry(window,width=48,show='*',
        textvariable=var_usr_passwd)
passwd_entry.place(x=120,y=190)

def login():
    usr_name = var_usr_name
    usr_passwd = var_usr_passwd
    try :
        with open('usrs_info.pickle','rb') as usr_file:
            usrs_info = pickle.load(usr_file)
    except :
        with open('usrs_info.pickle','wb') as usr_file:
            usrs_info = {'admin':'admin'}
            pickle.dump(usrs_info,usr_file)
    
    if usr_name in usrs_info:
        if usr_passwd == usrs_info[usr_name]:
            tk.messagebox.showinfo(title='Welcome', message='How are you' + usr_name)
        else :
            tk.messagebox.showerror(message='Error,your password is wrong')
    else :
        is_sign_up = tk.messagebox.askyesno(title='Welcome',
                message='You hvae not sign up yet. Sign up first.')
        if is_sign_up:
            usr_register()


def register():
    def ok():
        window_register.destroy()
    window_register = tk.Tk()
    window_register.title('Register')
    window_register.geometry('200x200')

    ok_button = tk.Button(window_register,text='ok',command=ok)
    ok_button.pack()

# login & register button
login_button = tk.Button(window,text='Login',command=login)
login_button.place(x=80,y=230)
regist_button = tk.Button(window,text='Register',command=register)
regist_button.place(x=280,y=230)

window.mainloop()
