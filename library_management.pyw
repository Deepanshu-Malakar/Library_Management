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

import pywinstyles
root=CTk()
pywinstyles.change_header_color(root,"blue")
pywinstyles.apply_style(root,"acrylic")

root.title("Library Management System")
root.geometry("500x400")

side_bar=CTkFrame(root,fg_color="blue",width=300,corner_radius=0)
side_bar.pack(padx=0,pady=0,side=LEFT,fill="y")

page=CTkFrame(root,fg_color="white",width=1600,corner_radius=0)
page.pack(side=LEFT,padx=0,pady=0,fill="both")


root.mainloop()
    
