from tkinter import *


class main_class():
    def __init__(self,student_profile):
        self.student_profile = student_profile
    def main_func(self):
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
        root.configure(bg='#fff')
        root.resizable(False,False)

        print(self.student_profile)
        img = PhotoImage(file='Untitled design (4).png')
        Label(root,image=img,bg='white').place(x=0,y=0)

        heading = Label(root,text="Account Details",bg='#9f6e6e',font=("Segoe UI", 20, "bold"))
        heading.place(x=320,y=50)
        # def list_organiser(student_profile):
        #     print(student_profile)


        roll_no = Label(root,text="Roll No. - "+str(self.student_profile[0]),bg='#9f6e6e',font=("Segoe UI", 12))
        roll_no.place(x=340,y=90)

        first_name = Label(root,text="First Name - "+str(self.student_profile[1]),bg='#9f6e6e',font=("Segoe UI", 12))
        first_name.place(x=340,y=120)

        last_name = Label(root,text="Last Name - "+str(self.student_profile[2]),bg='#9f6e6e',font=("Segoe UI", 12))
        last_name.place(x=340, y=150)

        DOB = Label(root,text="DOB - "+str(self.student_profile[3]),bg='#9f6e6e',font=("Segoe" ,12))
        DOB.place(x=340,y=180)

        father_name = Label(root,text="Father Name - "+str(self.student_profile[4]),bg='#9f6e6e',font=("Segoe UI", 12))
        father_name.place(x=340,y=210)

        mother_name = Label(root,text="Mother Name - "+str(self.student_profile[5]),bg='#9f6e6e',font=("Segoe UI", 12))
        mother_name.place(x=340,y=240)

        address = Label(root,text="Address - "+str(self.student_profile[6]),bg='#9f6e6e',font=("Segoe UI", 12))
        address.place(x=340,y=270)

        email = Label(root,text="Email - "+str(self.student_profile[7]),bg='#9f6e6e',font=("Segoe UI", 12))
        email.place(x=340,y=300)

        contact = Label(root,text="Contact - "+str(self.student_profile[8]),bg='#9f6e6e',font=("Segoe UI", 12))
        contact.place(x=340,y=330)

        HOD = Label(root,text="HOD - "+str(self.student_profile[9].split('(')[1].split(')')[0]),bg='#9f6e6e',font=("Segoe UI", 12))
        HOD.place(x=340,y=360)




        root.mainloop()
