from tkinter import *
from tkinter.ttk import Combobox,Treeview
from tkinter import messagebox
import mysql.connector as ms

def clear():
    roll.set("")
    name.set("")
    email.set("")
    gender.set("")
    contact.set("")
    dob.set("")
    address.set("")
    searchbox.set("")

def show_all():
    try:
        mydb = ms.connect(host='localhost', user='root', password='T@nuj1001', database='student_management_system')
        cur = mydb.cursor()
        s="SELECT * FROM student"
        cur.execute(s)
        res=cur.fetchall()
        mydb.close()
        if len(res)!=0:
            student_table.delete(*student_table.get_children())
            for i in res:
                student_table.insert("",END,values=i)
        clear()
    except:
        messagebox.showerror("Error","Error")

def search():
    try:
        id=int(searchbox.get())
        clear()
        mydb = ms.connect(host='localhost', user='root', password='T@nuj1001', database='student_management_system')
        cur = mydb.cursor()
        s = f"SELECT * FROM student WHERE Roll_No={id}"
        cur.execute(s)
        res = cur.fetchall()
        mydb.close()
        if len(res) != 0:
            student_table.delete(*student_table.get_children())
            for i in res:
                student_table.insert("", END, values=i)
                roll.set(i[0])
                name.set(i[1])
                email.set(i[2])
                gender.set(i[3])
                contact.set(i[4])
                dob.set(i[5])
                address.set(i[6])
        else:
            messagebox.showinfo("About","No Data Found")
    except:
        messagebox.showerror("Error","Error")

def add():
    try:
        id=int(roll.get())
        nam=name.get()
        em=email.get()
        gen=gender.get()
        con=contact.get()
        db=dob.get()
        addr=address.get()
        mydb = ms.connect(host='localhost', user='root', password='T@nuj1001', database='student_management_system')
        cur = mydb.cursor()
        s="INSERT INTO student VALUES (%s,%s,%s,%s,%s,%s,%s)"
        l=(id,nam,em,gen,con,db,addr)
        cur.execute(s,l)
        mydb.commit()
        mydb.close()
        show_all()
        messagebox.showinfo("Success", "Successfully Added")
    except:
        messagebox.showerror("Error","Error")

def update():
    try:
        id = int(roll.get())
        nam = name.get()
        em = email.get()
        gen = gender.get()
        con = contact.get()
        db = dob.get()
        addr = address.get()
        mydb = ms.connect(host='localhost', user='root', password='T@nuj1001', database='student_management_system')
        cur = mydb.cursor()
        s=f"UPDATE student SET Name='{nam}',Email='{em}',Gender='{gen}',Contact='{con}',Dob='{db}',Address='{addr}' WHERE Roll_No={id}"
        cur.execute(s)
        mydb.commit()
        mydb.close()
        clear()
        show_all()
        messagebox.showinfo("Success", "Successfully Updated")
    except:
        messagebox.showerror("Error","Error")

def delete():
    try:
        id = int(roll.get())
        mydb = ms.connect(host='localhost', user='root', password='T@nuj1001', database='student_management_system')
        cur = mydb.cursor()
        s = f"Delete FROM student WHERE Roll_No={id}"
        cur.execute(s)
        mydb.commit()
        mydb.close()
        clear()
        show_all()
        messagebox.showinfo("Success", "Successfully Deleted")
    except:
        messagebox.showerror("Error","Error")


root=Tk()
# root.geometry("-50+50")
root.title("STUDENT MANAGEMENT SYSTEM")

frame1=LabelFrame(root,width=100,bg='black')
frame1.grid(row=0,column=0,columnspan=2,sticky='NW')

heading=Label(frame1,text="Student Management System",font=('arial',40,'bold'),bg='lightblue',width=50)
heading.pack(side=TOP)

frame2=LabelFrame(root,bg="lightgrey",width=100)
frame2.grid(row=1,column=0,sticky='W')
h1=Label(frame2,text="Manage Students",font=('arial',30,'bold'),bg='lightgrey')
h1.grid(row=0,column=0,columnspan=2,pady=10)
label_layout=[("Roll No.",1,0),("Name",2,0),("Email",3,0),("Gender",4,0),("Contact",5,0),("D.O.B",6,0),("Address",7,0)]
for (t,r,c) in label_layout:
    lab=Label(frame2,text=t,font=("arial",20,'bold'),bg='lightgrey')
    lab.grid(row=r,column=c,sticky='W')

roll=StringVar()
roll.set("")
roll_entry=Entry(frame2,textvariable=roll,font=('arial',20),bg='white',width=21)
roll_entry.grid(row=1,column=1,padx=10,pady=20)

name=StringVar()
name.set("")
name_entry=Entry(frame2,textvariable=name,font=('arial',20),bg='white',width=21)
name_entry.grid(row=2,column=1,padx=10,pady=20)

email=StringVar()
email.set("")
email_entry=Entry(frame2,textvariable=email,font=('arial',20),bg='white',width=21)
email_entry.grid(row=3,column=1,padx=10,pady=20)

gender=StringVar()
gender.set("")
gender_combo=Combobox(frame2,values=('Male','Female','Other'),textvariable=gender,font=('arial',20),width=20)
gender_combo.grid(row=4,column=1,padx=10,pady=20)

contact=StringVar()
contact.set("")
contact_entry=Entry(frame2,textvariable=contact,font=('arial',20),bg='white',width=21)
contact_entry.grid(row=5,column=1,padx=10,pady=20)

dob=StringVar()
dob.set("")
dob_entry=Entry(frame2,textvariable=dob,font=('arial',20),bg='white',width=21)
dob_entry.grid(row=6,column=1,padx=10,pady=20)

address=StringVar()
address.set("")
address_entry=Entry(frame2,textvariable=address,font=('arial',20),bg='white',width=21)
address_entry.grid(row=7,column=1,padx=10,pady=20)

inner_frame2=LabelFrame(frame2,bg='black',relief="ridge",bd=3)
inner_frame2.grid(row=8,column=0,columnspan=2,pady=10)

add_button=Button(inner_frame2,text="Add",overrelief="groove",bd=5,font=('arial',10,'bold'),width=10,bg='red',command=add)
add_button.grid(row=0,column=0,padx=10,pady=10)

update_button=Button(inner_frame2,text="Update",overrelief="groove",bd=5,font=('arial',10,'bold'),width=10,bg='yellow',command=update)
update_button.grid(row=0,column=1,padx=10,pady=10)

delete_button=Button(inner_frame2,text="Delete",overrelief="groove",bd=5,font=('arial',10,'bold'),width=10,bg='red',command=delete)
delete_button.grid(row=0,column=2,padx=10,pady=10)

clear_button=Button(inner_frame2,text="Clear",overrelief="groove",bd=5,font=('arial',10,'bold'),width=10,bg='yellow',command=clear)
clear_button.grid(row=0,column=3,padx=10,pady=10)

frame3=LabelFrame(root,bg='lightgrey',width=100)
frame3.grid(row=1,column=1,sticky='N')

frame_inner_3=LabelFrame(frame3,bd=5,bg='lightgrey')
frame_inner_3.pack(side=TOP,fill=BOTH)

select_label=Label(frame_inner_3,text="Search By Roll No.",bg="lightgrey",font=('arial',20,'bold'))
select_label.grid(row=0,column=0,padx=10,pady=10)

searchbox=StringVar()
searchbox.set("")
box=Entry(frame_inner_3,textvariable=searchbox,font=('arial',20),bg='white',width=21,relief="groove",bd=3)
box.grid(row=0,column=1,padx=10,pady=10)

search_button=Button(frame_inner_3,text="Search",overrelief="sunken",bg='lightpink',font=('arial',12,'bold'),command=search)
search_button.grid(row=0,column=2,padx=10,pady=10)

show_all_button=Button(frame_inner_3,text="Show All",font=('arial',12,'bold'),bg='lightgreen',command=show_all)
show_all_button.grid(row=0,column=3,padx=10,pady=10)

inner_frame3=LabelFrame(frame3,bd=5,bg='lightgrey')
inner_frame3.pack(fill=BOTH)

x_scroll=Scrollbar(inner_frame3,orient=HORIZONTAL)
y_scroll=Scrollbar(inner_frame3,orient=VERTICAL)

head=("Roll No.","Name","Email","Gender","Contact","D.O.B.","Address")
student_table=Treeview(inner_frame3,columns=head,yscrollcommand=y_scroll.set,xscrollcommand=x_scroll.set,height=28)
x_scroll.config(command=student_table.xview)
y_scroll.config(command=student_table.yview)
x_scroll.pack(side=BOTTOM,fill=X)
y_scroll.pack(side=RIGHT,fill=Y)
student_table.pack(fill=BOTH)

for text in head:
    student_table.heading(text,text=text)

student_table['show']='headings'

for text in head:
    student_table.column(text,width=100)

show_all()

root.mainloop()
