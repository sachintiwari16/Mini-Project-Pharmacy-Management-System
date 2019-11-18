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

        DateofOrder = StringVar()
        DateofOrder.set(time.strftime("%d/%m/%Y"))

        var1 = StringVar()
        var2 = StringVar()
        var3 = StringVar()
        var4 = IntVar()

        Firstname = StringVar()
        Surname = StringVar()
        Address = StringVar()
        Postcode = StringVar()
        Telephone = StringVar()
        Ref = StringVar()

        Membership = StringVar()
        Membership.set("0")

        # ============================Frame=======================================

        def iExit():
            iExit = tkinter.messagebox.askyesno("Patient Registration System", "Confirm if you want to exit")
            if iExit > 0:
                self.master.destroy()
                return

        def Reset():
            Firstname.set("")
            Surname.set("")
            Address.set("")
            Postcode.set("")
            Telephone.set("")
            Ref.set("")
            Membership.set("0")

            var1.set("")
            var2.set("")
            var3.set("")
            var4.set(0)

            self.cboProve_of_ID.current(0)
            self.cboType_Of_Member.current(0)
            self.cboMethod_of_Payment.current(0)
            self.txtMembership.config(state=DISABLED)

        def iResetRecord():
            iResetRecord = tkinter.messagebox.askokcancel("Patient Registration System",
                                                          "Confirm if you want to add a new record")
            if iResetRecord > 0:
                Reset()
            elif iResetRecord <= 0:
                Reset()
                self.txtReceipt.delete("1.0", END)
                return

        def Ref_No():
            x = random.randint(10903, 600873)
            randomRef = str(x)
            Ref.set(randomRef)

        def Receipt():
            Ref_No()
            self.txtReceipt.insert(END,
                                   "\t" + Ref.get() + "\t\t" + Firstname.get() + "\t\t" + Surname.get() + "\t\t" + Address.get() + "\t\t" + DateofOrder.get() + "\t\t" + Telephone.get() + "\t\t" + Membership.get() + "\n")

        def Membership_Fees():

            if (var4.get() == 1):
                self.txtMembership.configure(state=NORMAL)
                Item1 = float(50)
                Membership.set("Rs" + str(Item1))

            elif (var4.get() == 0):
                self.txtMembership.configure(state=DISABLED)
                Membership.set("0")

        # ============================Frame=======================================

        Mainframe = Frame(self.frame)
        Mainframe.grid()

        TitleFrame = Frame(Mainframe, bd=20, width=1350, padx=26, relief=RIDGE)
        TitleFrame.pack(side=TOP)

        self.lblTitle = Label(TitleFrame, font=('arial', 59, 'bold'), text="Patient Registration System", padx=2)
        self.lblTitle.grid()
        # ============================LowerFrames=======================================
        MemberDetailsFrame = LabelFrame(Mainframe, width=1350, height=500, bd=20, pady=5, relief=RIDGE)
        MemberDetailsFrame.pack(side=BOTTOM)

        FrameDetails = LabelFrame(MemberDetailsFrame, bd=10, width=880, height=400, relief=RIDGE)
        FrameDetails.pack(side=LEFT)

        MembersName_F = LabelFrame(FrameDetails, bd=10, width=350, height=400, font=('arial', 12, 'bold'),
                                   text="Customer Name", relief=RIDGE)
        MembersName_F.grid(row=0, column=0)

        Receipt_ButtonFrame = LabelFrame(MemberDetailsFrame, bd=10, width=1000, height=400, relief=RIDGE)
        Receipt_ButtonFrame.pack(side=RIGHT)
        # ============================LowerFrames=======================================

        self.lblReferenceNo = Label(MembersName_F, font=('arial', 14, 'bold'), text="Reference No", bd=7)
        self.lblReferenceNo.grid(row=0, column=0, sticky=W)
        self.txtReferenceNo = Entry(MembersName_F, font=('arial', 14, 'bold'), bd=7, textvariable=Ref, state=DISABLED,
                                    insertwidth=2)
        self.txtReferenceNo.grid(row=0, column=1)

        self.lblFirstName = Label(MembersName_F, font=('arial', 14, 'bold'), text="First Name", bd=7)
        self.lblFirstName.grid(row=1, column=0, sticky=W)
        self.FirstName = Entry(MembersName_F, font=('arial', 14, 'bold'), bd=7, insertwidth=2, textvariable=Firstname)
        self.FirstName.grid(row=1, column=1)

        self.lblSurname = Label(MembersName_F, font=('arial', 14, 'bold'), text="Surname", bd=7)
        self.lblSurname.grid(row=2, column=0, sticky=W)
        self.Surname = Entry(MembersName_F, font=('arial', 14, 'bold'), bd=7, insertwidth=2, textvariable=Surname)
        self.Surname.grid(row=2, column=1)

        self.lblAddress = Label(MembersName_F, font=('arial', 14, 'bold'), text="Address", bd=7)
        self.lblAddress.grid(row=3, column=0, sticky=W)
        self.Address = Entry(MembersName_F, font=('arial', 14, 'bold'), bd=7, insertwidth=2, textvariable=Address)
        self.Address.grid(row=3, column=1)

        self.lblPostCode = Label(MembersName_F, font=('arial', 14, 'bold'), text="PostCode", bd=7)
        self.lblPostCode.grid(row=4, column=0, sticky=W)
        self.PostCode = Entry(MembersName_F, font=('arial', 14, 'bold'), bd=7, insertwidth=2, textvariable=Postcode)
        self.PostCode.grid(row=4, column=1)

        self.lblTelephone = Label(MembersName_F, font=('arial', 14, 'bold'), text="Telephone", bd=7)
        self.lblTelephone.grid(row=5, column=0, sticky=W)
        self.Telephone = Entry(MembersName_F, font=('arial', 14, 'bold'), bd=7, insertwidth=2, textvariable=Telephone)
        self.Telephone.grid(row=5, column=1)

        self.lblDate = Label(MembersName_F, font=('arial', 14, 'bold'), text="Date", bd=7)
        self.lblDate.grid(row=6, column=0, sticky=W)
        self.Date = Entry(MembersName_F, font=('arial', 14, 'bold'), bd=7, insertwidth=2, textvariable=DateofOrder)
        self.Date.grid(row=6, column=1)
        # ============================Member Information==========================================================
        self.lblProve_of_ID = Label(MembersName_F, font=('arial', 14, 'bold'), text="Prove of ID", bd=7)
        self.lblProve_of_ID.grid(row=7, column=0, sticky=W)

        self.cboProve_of_ID = ttk.Combobox(MembersName_F, textvariable=var1, state='readonly',
                                           font=('arial', 14, 'bold'), width=19)
        self.cboProve_of_ID['value'] = ('', 'Aadhar Card', 'Driving Licence', 'Passort', 'Student ID')
        self.cboProve_of_ID.current(0)
        self.cboProve_of_ID.grid(row=7, column=1)

        self.lblType_Of_Member = Label(MembersName_F, font=('arial', 14, 'bold'), text="Type Of Member", bd=7)
        self.lblType_Of_Member.grid(row=8, column=0, sticky=W)

        self.cboType_Of_Member = ttk.Combobox(MembersName_F, textvariable=var2, state='readonly',
                                              font=('arial', 14, 'bold'), width=19)
        self.cboType_Of_Member['value'] = ('', 'Full Member', 'Annual Membership', 'Pay as you Go', 'Honorary Member')
        self.cboType_Of_Member.current(0)
        self.cboType_Of_Member.grid(row=8, column=1)

        self.lblMethod_of_Payment = Label(MembersName_F, font=('arial', 14, 'bold'), text="Method of Payment", bd=7)
        self.lblMethod_of_Payment.grid(row=9, column=0, sticky=W)

        self.cboMethod_of_Payment = ttk.Combobox(MembersName_F, textvariable=var3, state='readonly',
                                                 font=('arial', 14, 'bold'), width=19)
        self.cboMethod_of_Payment['value'] = ('', 'Visa Card', 'Master Card', 'Debit Card', 'Cash')
        self.cboMethod_of_Payment.current(0)
        self.cboMethod_of_Payment.grid(row=9, column=1)

        # ============================Check Button==========================================================

        self.chkMembership = Checkbutton(MembersName_F, text="Patient Fees", variable=var4, onvalue=1, offvalue=0,
                                         font=('arial', 16, 'bold'), command=Membership_Fees)
        self.chkMembership.grid(row=10, column=0, sticky=W)

        self.txtMembership = Entry(MembersName_F, textvariable=Membership, bd=7, insertwidth=2, state=DISABLED,
                                   justify=RIGHT)
        self.txtMembership.grid(row=10, column=1)

        # ===================================Receipt==============================================================

        self.lblLabel = Label(Receipt_ButtonFrame, font=('arial', 10, 'bold'), pady=10,
                              text="Patient Ref\t Firstname\t Surname\t Address\t\t Date of Reg.\t Telephone\t Patient Paid",
                              bd=7)
        self.lblLabel.grid(row=0, column=0, columnspan=4)

        self.txtReceipt = Text(Receipt_ButtonFrame, width=112, height=22, font=('arial', 10, 'bold'))
        self.txtReceipt.grid(row=1, column=0, columnspan=4)

        # ===================================Buttons==============================================================

        self.btnReceipt = Button(Receipt_ButtonFrame, padx=18, bd=7, font=('arial', 16, 'bold'), width=13,
                                 text="Receipt", command=Receipt).grid(row=2, column=0)
        self.btnReset = Button(Receipt_ButtonFrame, padx=18, bd=7, font=('arial', 16, 'bold'), width=13, text="Reset",
                               command=iResetRecord).grid(row=2, column=1)
        self.btnExit = Button(Receipt_ButtonFrame, padx=18, bd=7, font=('arial', 16, 'bold'), width=13, text="Exit",
                              command=iExit).grid(row=2, column=2)

        self.quitButton = Button(self.frame, width=25, text="Quit", command=iExit)
        self.quitButton.grid(row=3, column=0)

    def close_window(self):
        self.master.destroy()

    def iExit():
        self.iExit = tkinter.messagebox.askyesno("Patients Registration System", "Confir if you want to exit")
        if self.iExit > 0:
            self.master.destroy()
        else:
            self.newWindow = Toplevel(self.master)
            self.app = Window2(self.newWindow)
            return

        # ========================================================================================================


class Window3:
    def __init__(self, master):
        self.master = master
        self.master.title("Hospital Management System")
        self.master.geometry('1350x750+0+0')
        self.frame = Frame(self.master)
        self.frame.pack()


if __name__ == '__main__':
    main()
