
#Riddhi

from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk 


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
        
        
if __name__=="__main__" :
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()
           