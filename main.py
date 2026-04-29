import tkinter as tk

from home_screen import homescreen
from lower_food_court import lowerfoodcourt
from search import searchscreen
from map import mapscreen

class TraffordKiosk:

    def __init__(self,root):
        self.root = root
        self.root.title('Trafford Centre Kiosk')
        self.root.geometry('1080x1340')
        self.current_screen = None
        self.show_home()
        
        
    def show_home(self):
        self.switch_to(homescreen)

    def show_foodcourt(self):
        self.switch_to(lowerfoodcourt)

    def show_searchscreen(self):
        self.switch_to(searchscreen)
    
    def show_mapscreen(self):
        self.switch_to(mapscreen)
        
    def switch_to(self, ScreenClass):
        if self.current_screen is not None:
            self.current_screen.frame.destroy()
        self.current_screen = ScreenClass(self.root, self)    

if __name__ == '__main__':
    root = tk.Tk()
    app = TraffordKiosk(root)
    root.mainloop()