from tkinter import *
import qrcode
from PIL import Image, ImageTk
from resizeimage import resizeimage

class Qr_Generator:  
    def __init__(self, root):
      
        self.root = root
        self.root.geometry("900x500+200+50")
        self.root.title("QR Generator")
        self.root.resizable(True, True)

        title = Label(self.root, text="QR Code Generator", font=("times new roman", 40), bg='#053246', fg='white', anchor='w').place(x=0, y=0, relwidth=1)

        #===========Employee details window==============
        #=========variable==========
        self.var_emp_code = StringVar()
        self.var_emp_name = StringVar()
        self.var_emp_department = StringVar()
        self.var_emp_designation = StringVar()

        emp_Frame = Frame(self.root, bd=2, relief=RIDGE, bg='white')
        emp_Frame.place(x=50, y=100, width=500, height=380) 

        emp_title = Label(emp_Frame, text="Employee Details", font=("goudy old style", 30), bg='#043256', fg='white').place(x=0, y=0, relwidth=1)

        lbl_emp_code = Label(emp_Frame, text="Employee ID", font=("times new roman", 15, 'bold'), bg='white').place(x=20, y=60)
        lbl_name = Label(emp_Frame, text="Name", font=("times new roman", 15, 'bold'), bg='white').place(x=20, y=100)
        lbl_department = Label(emp_Frame, text="Department", font=("times new roman", 15, 'bold'), bg='white').place(x=20, y=140)
        lbl_designation = Label(emp_Frame, text="Designation", font=("times new roman", 15, 'bold'), bg='white').place(x=20, y=180)

        txt_emp_code = Entry(emp_Frame, font=("times new roman", 15), textvariable=self.var_emp_code, bg='lightyellow').place(x=200, y=60)
        txt_name = Entry(emp_Frame, font=("times new roman", 15), textvariable=self.var_emp_name, bg='lightyellow').place(x=200, y=100)
        txt_department = Entry(emp_Frame, font=("times new roman", 15), textvariable=self.var_emp_department, bg='lightyellow').place(x=200, y=140)
        txt_designation = Entry(emp_Frame, font=("times new roman", 15), textvariable=self.var_emp_designation, bg='lightyellow').place(x=200, y=180)

        btn_generate = Button(emp_Frame, text='QR Generate', command=self.generate, font=("times new roman", 18, 'bold'), bg='#2196f3', fg='white').place(x=90, y=250, width=170, height=30)
        btn_clear = Button(emp_Frame, text='Clear', command=self.clear, font=("times new roman", 18, 'bold'), bg='#607d8b', fg='white').place(x=280, y=250, width=170, height=30)

        self.msg = ''
        self.lbl_msg = Label(emp_Frame, text=self.msg, font=("times new roman", 15, 'bold'), bg='white', fg='green')
        self.lbl_msg.place(x=0, y=310, relwidth=1)

        #===========Employee QR Code window==============
        qr_Frame = Frame(self.root, bd=2, relief=RIDGE, bg='white')
        qr_Frame.place(x=600, y=100, width=250, height=380) 

        emp_title = Label(qr_Frame, text="Employee QR Code", font=("goudy old style", 20), bg='#043256', fg='white').place(x=0, y=0, relwidth=1)

        self.qr_code = Label(qr_Frame, text='No QR\nAvailable', font=('times new roman', 15), bg='#3f51b5', fg='white', bd=1, relief=RIDGE)
        self.qr_code.place(x=35, y=100, width=180, height=180)

    def clear(self):
        self.var_emp_code.set('')
        self.var_emp_name.set('')
        self.var_emp_department.set('')
        self.var_emp_designation.set('')
        self.msg = ''
        self.lbl_msg.config(text=self.msg) 
        self.qr_code.config(image='')

    def generate(self):
        if self.var_emp_designation.get() == '' or self.var_emp_code.get() == '' or self.var_emp_department.get() == '' or self.var_emp_name.get() == '':
            self.msg = 'All fields are required!!!'
            self.lbl_msg.config(text=self.msg, fg='red')  
        else:
            qr_data = (f"Employee ID: {self.var_emp_code.get()}\nEmployee name:{self.var_emp_name.get()}\nDepartment: {self.var_emp_department.get()}\nDesignation: {self.var_emp_designation.get()}")
            qr_code = qrcode.make(qr_data)
            print(qr_code)
            qr_code = resizeimage.resize_cover(qr_code, [180, 180])
            
            #=============QR Code Image Update============
            self.im = ImageTk.PhotoImage(qr_code)
            self.qr_code.config(image=self.im)

            #=============updating notification============
            self.msg = 'QR Generated Successfully!!!'
            self.lbl_msg.config(text=self.msg, fg='green')  

root = Tk()
obj = Qr_Generator(root)
root.mainloop()
