#Riddhi

from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk 
from student import Student

class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1536x800+0+0")
        self.root.title("Face Recognition System")
        
        """
        img=Image.open("images/trial1.jpg")
        img=img.resize((511,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)
        
        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=511,height=130)
        
        img1=Image.open("images/trial1.jpg")
        img1=img1.resize((511,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=511,y=0,width=511,height=130)
        
        img2=Image.open("images/trial1.jpg")
        img2=img2.resize((511,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=511,height=130)   """
        
        img3=Image.open("images/trial1.jpg")
        img3=img3.resize((1536,800),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=0,width=1536,height=800)
        
        title_lbl=Label(bg_img,text="Face Recognition Attendance System",font=("times new roman",35,"bold"),bg="white")
        title_lbl.place(x=0,y=0,width=1536,height=45)
        
        
        #student button
        img4=Image.open("images/studentdetails.jpg")
        img4=img4.resize((220,220),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        
        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=150,width=220,height=220)
        
        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="black",fg="white")
        title_lbl.place(x=0,y=0,width=1536,height=45)
        b1_1.place(x=200,y=350,width=220,height=40)
        
        
        #detect face button
        img5=Image.open("images/trial1.jpg")
        img5=img5.resize((220,220),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)
        
        b1=Button(bg_img,image=self.photoimg4,cursor="hand2")
        b1.place(x=500,y=150,width=220,height=220)
        
        b1_1=Button(bg_img,text="Face Detector",cursor="hand2",font=("times new roman",15,"bold"),bg="black",fg="white")
        title_lbl.place(x=0,y=0,width=1536,height=45)
        b1_1.place(x=500,y=350,width=220,height=40)
        
        
        #attendance button
        img6=Image.open("images/trial1.jpg")
        img6=img6.resize((220,220),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)
        
        b1=Button(bg_img,image=self.photoimg4,cursor="hand2")
        b1.place(x=800,y=150,width=220,height=220)
        
        b1_1=Button(bg_img,text="Attendance",cursor="hand2",font=("times new roman",15,"bold"),bg="black",fg="white")
        title_lbl.place(x=0,y=0,width=1536,height=45)
        b1_1.place(x=800,y=350,width=220,height=40)
        
        
        #help button
        img7=Image.open("images/trial1.jpg")
        img7=img7.resize((220,220),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)
        
        b1=Button(bg_img,image=self.photoimg4,cursor="hand2")
        b1.place(x=1100,y=150,width=220,height=220)
        
        b1_1=Button(bg_img,text="Help",cursor="hand2",font=("times new roman",15,"bold"),bg="black",fg="white")
        title_lbl.place(x=0,y=0,width=1536,height=45)
        b1_1.place(x=1100,y=350,width=220,height=40)
        
        #train face button
        img8=Image.open("images/trial1.jpg")
        img8=img8.resize((220,220),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)
        
        b1=Button(bg_img,image=self.photoimg4,cursor="hand2")
        b1.place(x=200,y=450,width=220,height=220)
        
        b1_1=Button(bg_img,text="Train Face",cursor="hand2",font=("times new roman",15,"bold"),bg="black",fg="white")
        title_lbl.place(x=0,y=0,width=1536,height=45)
        b1_1.place(x=200,y=650,width=220,height=40)
        
        #photos button
        img9=Image.open("images/trial1.jpg")
        img9=img9.resize((220,220),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)
        
        b1=Button(bg_img,image=self.photoimg4,cursor="hand2")
        b1.place(x=500,y=450,width=220,height=220)
        
        b1_1=Button(bg_img,text="Photos",cursor="hand2",font=("times new roman",15,"bold"),bg="black",fg="white")
        title_lbl.place(x=0,y=0,width=1536,height=45)
        b1_1.place(x=500,y=650,width=220,height=40)
        
        #developer button
        img9=Image.open("images/trial1.jpg")
        img9=img9.resize((220,220),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)
        
        b1=Button(bg_img,image=self.photoimg4,cursor="hand2")
        b1.place(x=800,y=450,width=220,height=220)
        
        b1_1=Button(bg_img,text="Developer",cursor="hand2",font=("times new roman",15,"bold"),bg="black",fg="white")
        title_lbl.place(x=0,y=0,width=1536,height=45)
        b1_1.place(x=800,y=650,width=220,height=40)
        
        #exit button
        img10=Image.open("images/trial1.jpg")
        img10=img10.resize((220,220),Image.ANTIALIAS)
        self.photoimg10=ImageTk.PhotoImage(img10)
        
        b1=Button(bg_img,image=self.photoimg4,cursor="hand2")
        b1.place(x=1100,y=450,width=220,height=220)
        
        b1_1=Button(bg_img,text="Exit",cursor="hand2",font=("times new roman",15,"bold"),bg="black",fg="white")
        title_lbl.place(x=0,y=0,width=1536,height=45)
        b1_1.place(x=1100,y=650,width=220,height=40)

#Function Button
    def student_details(self):
        self.new_window=Toplebel(self.root)
        self.app=Student(self.new_window)
        
if __name__=="__main__" :
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()

