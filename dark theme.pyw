class Book:
    def __init__(self,title,author,year) -> None:
        self.title=title
        self.author=author
        self.publication_year=year
        self.copies_available=1
        self.borrow_history=[]

    def __str__(self) -> str:
        return f"{self.title} published by {self.author} in year {self.publication_year}"
    
    def check_availability(self):
        return self.copies_available>0
    
    def checkout(self,borrower):
        if self.copies_available>0:
            self.copies_available-=1
            self.borrow_history.append(borrower)
        else:
            return f"no copies of {self.title} available :("
        pass

    def checkin(self):
        self.copies_available+=1
        pass
    

from tkinter import *
from customtkinter import *
from PIL import Image
import pywinstyles
root=CTk()
# pywinstyles.change_header_color(root,"#0D99FF")
# pywinstyles.apply_style(root,"acrylic")

root.title("Library Management System")
root.geometry("500x400")

set_appearance_mode("dark")

navbar=CTkFrame(root,height=100,corner_radius=0)
navbar.pack(side=TOP,padx=0,pady=0,fill="x")

navbar_center=CTkFrame(navbar,fg_color="transparent")
navbar_center.pack()

class Navbar:
    def __init__(self,img,img2,name="") -> None:
        self.button=CTkButton(navbar_center,text=name,image=img2,width=30,fg_color="transparent",text_color="#B3B3B3")
        self.button.pack(side=LEFT,padx=10,pady=5)

        self.selected=img
        self.unselected=img2

    def click(self):
        self.button.configure(image=self.selected,text_color="white")
        self.frame=CTkFrame(root,fg_color="transparent")
        self.frame.pack()


home_icon1=CTkImage(Image.open(r"icons\home selected.png"),size=(30,30))    
home_icon2=CTkImage(Image.open(r"icons\home unselected2.png"),size=(30,30))    

home=Navbar(home_icon1,home_icon2,"Home")

def delete_all_frames():
    try:
        home.frame.destroy()
    except:
        pass
    try:
        add.frame.destroy()
    except:
        pass
    try:
        history.frame.destroy()
    except:
        pass
    try:
        search.frame.destroy()
    except:
        pass

def unselect_all():
    add.button.configure(image=add.unselected,text_color="#B3B3B3")
    home.button.configure(image=home.unselected,text_color="#B3B3B3")
    history.button.configure(image=history.unselected,text_color="#B3B3B3")
    search.button.configure(image=search.unselected,text_color="#B3B3B3")


def home_page():
    delete_all_frames()
    unselect_all()
    home.click()
    # add.button.configure(image=add.unselected)
home.button.configure(command=home_page)

add_icon1=CTkImage(Image.open(r"icons\add selected.png"),size=(30,30))    
add_icon2=CTkImage(Image.open(r"icons\add unselected2.png"),size=(30,30))    

add=Navbar(add_icon1,add_icon2,"Add Book")
def add_page():
    delete_all_frames()
    unselect_all()
    add.click()
    # home.button.configure(image=home.unselected)
add.button.configure(command=add_page)


history_icon1=CTkImage(Image.open(r"icons\history selected.png"),size=(30,30))    
history_icon2=CTkImage(Image.open(r"icons\history unselected2.png"),size=(30,30)) 

history=Navbar(history_icon1,history_icon2,"History")
def history_page():
    delete_all_frames()
    unselect_all()
    history.click()
    # home.button.configure(image=home.unselected)
history.button.configure(command=history_page)

search_icon1=CTkImage(Image.open(r"icons\search selected.png"),size=(30,30))    
search_icon2=CTkImage(Image.open(r"icons\search unselected2.png"),size=(30,30)) 

search=Navbar(search_icon1,search_icon2,"Search")
def search_page():
    delete_all_frames()
    unselect_all()
    search.click()
    # home.button.configure(image=home.unselected)
search.button.configure(command=search_page)

root.mainloop()
    
