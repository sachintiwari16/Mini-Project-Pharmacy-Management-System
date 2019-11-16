from tkinter import *
import tkinter.messagebox
from tkinter import ttk
import random
import time;
import datetime


def main():
    root = Tk()
    app = Window1(root)


class Window1:
    def __init__(self, master):
        self.master = master
        self.master.title("Pharmacy Management System")
        self.master.geometry('1350x750+0+0')
        self.frame = Frame(self.master)
        self.frame.pack()

        self.Username = StringVar()
        self.Password = StringVar()

        self.LabelTitle = Label(self.frame, text='Pharmacy Management System', font=('arial', 50, 'bold'), bd=20)
        self.LabelTitle.grid(row=0, column=0, columnspan=2)

        self.Loginframe1 = Frame(self.frame, width=1010, height=300, bd=20, relief='ridge')
        self.Loginframe1.grid(row=1, column=0)

        self.Loginframe2 = Frame(self.frame, width=1000, height=100, bd=20, relief='ridge')
        self.Loginframe2.grid(row=2, column=0)

        self.Loginframe3 = Frame(self.frame, width=1000, height=200, bd=20, relief='ridge')
        self.Loginframe3.grid(row=3, column=0)
        # ===========================================================================================================================

        self.lblUsername = Label(self.Loginframe1, text='Username', font=('arial', 50, 'bold'), bd=22)
        self.lblUsername.grid(row=0, column=0)
        self.txtUsername = Entry(self.Loginframe1, font=('arial', 50, 'bold'), textvariable=self.Username, bd=22)
        self.txtUsername.grid(row=0, column=1)

        self.lblPassword = Label(self.Loginframe1, text='Password', font=('arial', 50, 'bold'), bd=22)
        self.lblPassword.grid(row=1, column=0)
        self.txtPassword = Entry(self.Loginframe1, font=('arial', 50, 'bold'), textvariable=self.Password, bd=22)
        self.txtPassword.grid(row=1, column=1)
        # ===========================================================================================================================

        self.btnLogin = Button(self.Loginframe2, text='Login', width=17, font=('arial', 20, 'bold'),
                               command=self.Login_System)
        self.btnLogin.grid(row=0, column=0)

        self.btnReset = Button(self.Loginframe2, text='Reset', width=17, font=('arial', 20, 'bold'), command=self.Reset)
        self.btnReset.grid(row=0, column=1)

        self.btnExit = Button(self.Loginframe2, text='Exit', width=17, font=('arial', 20, 'bold'), command=self.iExit)
        self.btnExit.grid(row=0, column=2)
        # ===========================================================================================================================

        self.btnRegistration = Button(self.Loginframe3, text='Patients Registration System', font=('arial', 20, 'bold'),
                                      state=DISABLED, command=self.Registration_window)
        self.btnRegistration.grid(row=0, column=0)

        self.btnHospital = Button(self.Loginframe3, text='Hospital Management System', font=('arial', 20, 'bold'),
                                  state=DISABLED, command=self.Hospital_window)
        self.btnHospital.grid(row=0, column=1)

    # ===========================================================================================================================
    def Login_System(self):
        user = (self.Username.get())
        pas = (self.Password.get())

        if (user == str(1234)) and (pas == str(2345)):
            self.btnRegistration.config(state=NORMAL)
            self.btnHospital.config(state=NORMAL)
        else:
            tkinter.messagebox.askyesno("Pharmacy Management System", "You have entered an invalid login details")
            self.btnRegistration.config(state=DISABLED)
            self.btnHospital.config(state=DISABLED)
            self.Username.set("")
            self.Password.set("")
            self.txtUsername.focus()

    def Reset(self):
        self.btnRegistration.config(state=DISABLED)
        self.btnHospital.config(state=DISABLED)
        self.Username.set("")
        self.Password.set("")
        self.txtUsername.focus()

    def iExit(self):
        self.iExit = tkinter.messagebox.askyesno("Pharmacy Management System", "Confirm if you want to exit")
        if self.iExit > 0:
            self.master.destroy()
            return

    # ===========================================================================================================================
    def Registration_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = Window2(self.newWindow)

    def Hospital_window(self):
        self.newWindow = Toplevel(self.master)
        self.app = Window3(self.newWindow)


class Window2:
    def __init__(self, master):
        self.master = master
        self.master.title("Patients Registration System")
        self.master.geometry('1350x750+0+0')
        self.frame = Frame(self.master)
        self.frame.pack()


class Window3:
    def __init__(self, master):
        self.master = master
        self.master.title("Hospital Management System")
        self.master.geometry('1350x750+0+0')
        self.frame = Frame(self.master)
        self.frame.pack()


if __name__ == '__main__':
    main()
