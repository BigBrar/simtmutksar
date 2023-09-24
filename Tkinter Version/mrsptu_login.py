import second_page
import threading
import send_input
from tkinter import *
from tkinter.messagebox import showerror, showwarning, showinfo
import time

student_profile = None

done = False

root = Tk()
root.title('Login')
w= 925 # width for the Tk root
h = 500 # height for the Tk root

# get screen width and height
ws = root.winfo_screenwidth() # width of the screen
hs = root.winfo_screenheight() # height of the screen

# calculate x and y coordinates for the Tk root window
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

# set the dimensions of the screen
# and where it is placed
root.geometry('%dx%d+%d+%d' % (w, h, x, y))
# root.geometry('925x500+300+200')
root.configure(bg='#fff')
root.resizable(False,False)

img = PhotoImage(file='login.png')
Label(root,image=img,bg='white').place(x=50,y=50)

frame = Frame(root,width=350,height=350,bg='white')
frame.place(x=480,y=70)

heading=Label(frame,text='Sign in',fg='#57a1f8',bg='white',font=('Microsoft YaHei UI Light',23,'bold'))
heading.place(x=100,y=5)

##----------------------------------

def on_enter(e):
    name = user.get()
    if name != "Username":
        pass
    else:
        user.delete(0,'end')

def on_leave(e):
    name=user.get()
    if name=='':
        user.insert(0,'Username')


user=Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
user.place(x=30,y=80)
user.insert(0,'Username')
user.bind('<FocusIn>',on_enter)
user.bind('<FocusOut>',on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)

##----------------------------------

def update_loading_label():
    print("Entered function")
    global done
    dot=''
    while not done:
        time.sleep(0.3)
        if len(dot) == 5:
            print('limit reached')
            dot=''
        new_label.config(text='Loading'+dot)
        root.update()
        dot+='.'

def get_student_data(username,password):
    global done
    global student_profile
    object = send_input.mrsptu_details(username,password)
    student_profile = object.get_student_profile()
    # print(student_profile)
    done = True

def signin():
    global student_profile
    username = user.get()
    password = code.get()
    if username != '' and password != '' and username != 'Username' and password != 'Password':
        get_thread = threading.Thread(target=lambda: get_student_data(username,password))

        # Start the loading label update in the main thread
        get_thread.start()
        update_loading_label()
        # Wait for the GET request thread to finish
        get_thread.join()

        root.destroy()
        object = second_page.main_class(student_profile)
        object.main_func()

    else:
        showwarning("Empty Fields", "Both fields are required")
        root.destroy()


def on_enter(e):
    name = code.get()
    if name != "Password":
        pass
    else:
        code.delete(0,'end')

def on_leave(e):
    name=code.get()
    if name=='':
        code.insert(0,'Password')

code=Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Light',11))
code.place(x=30,y=150)
code.insert(0,'Password')
code.bind('<FocusIn>',on_enter)
code.bind('<FocusOut>',on_leave)


Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)

##----------------------------------

Button(frame,width=39,pady=7,text='Login',bg='#57a1f8',fg='white',border=0,command=signin).place(x=15,y=204)

new_label = Label(root,text=' ',fg='#57a1f8',bg='white',font=('Microsoft YaHei UI Light',15,'bold'))
new_label.place(x=370,y=425)



root.mainloop()
