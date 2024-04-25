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
pywinstyles.apply_style(root,"aero")


root.mainloop()
    
