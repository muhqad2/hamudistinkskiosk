import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import base64
from io import BytesIO


class homescreen:
    def __init__(self, root, app):
        self.root = root
        self.app = app
        self.root.title("Home Screen")
        self.root.geometry("1080x1340")
        self.root.resizable(True, True)
        
        # Initialize variables
        
        # Create widgets
        self._create_widgets()
    
    def _create_widgets(self):
        """Create and place all widgets"""
        self.frame = tk.Frame(self.root, width = 1080, height = 1340)
        self.frame.place(x=0, y=0)

        # map_button
        self.map_button = tk.Button(
            self.root,
            text="Map",
            font=("Arial", 38),
            command=self.on_map_button_click
        )
        self.map_button.place(x=190, y=320, width=360, height=130)
        
        # help_button
        self.help_button = tk.Button(
            self.root,
            text="Help",
            font=("Arial", 38),
            command=self.on_help_button_click
        )
        self.help_button.place(x=610, y=650, width=360, height=130)
        
        # up_floor_button
        self.up_floor_button = tk.Button(
            self.root,
            text="Upper Food Court",
            font=("Arial", 34),
            command=self.on_up_floor_button_click
        )
        self.up_floor_button.place(x=190, y=650, width=360, height=130)
        
        # park_button
        self.park_button = tk.Button(
            self.root,
            text="Parking",
            font=("Arial", 38),
            command=self.on_park_button_click
        )
        self.park_button.place(x=190, y=480, width=360, height=130)
        
        # low_floor_button
        self.low_floor_button = tk.Button(
            self.root,
            text="Lower Food Court",
            font=("Arial", 34),
            command=self.on_low_floor_button_click
        )
        self.low_floor_button.place(x=610, y=480, width=360, height=130)
        
        # store_button
        self.store_button = tk.Button(
            self.root,
            text="Stores",
            font=("Arial", 38),
            command=self.on_store_button_click
        )
        self.store_button.place(x=610, y=320, width=360, height=130)
        
        # frame_1
        self.frame_1 = tk.Frame(
            self.root,
            bg="#f3f4f6",
            relief="groove",
            bd=1
        )
        self.frame_1.place(x=0, y=0, width=170, height=650)
        
        # eng_lang
        self.eng_lang = tk.Button(
            self.root,
            text="English",
            font=("Arial", 27),
            command=self.on_eng_lang_click
        )
        self.eng_lang.place(x=20, y=90, width=130, height=90)
        
        # dutch_button
        self.dutch_button = tk.Button(
            self.root,
            text="Dutch",
            font=("Arial", 27),
            command=self.on_dutch_button_click
        )
        self.dutch_button.place(x=20, y=530, width=130, height=90)
        
        # germ_button
        self.germ_button = tk.Button(
            self.root,
            text="German",
            font=("Arial", 27),
            command=self.on_germ_button_click
        )
        self.germ_button.place(x=20, y=420, width=130, height=90)
        
        # french_lang
        self.french_lang = tk.Button(
            self.root,
            text="French",
            font=("Arial", 27),
            command=self.on_french_lang_click
        )
        self.french_lang.place(x=20, y=310, width=130, height=90)
        
        # span_button
        self.span_button = tk.Button(
            self.root,
            text="Español",
            font=("Arial", 27),
            command=self.on_span_button_click
        )
        self.span_button.place(x=20, y=200, width=130, height=90)
        
        # tc_logo
        # Load image for tc_logo
        self.tc_logo_photo = tk.PhotoImage(file="assets/tc_logo.png")
        self.tc_logo = tk.Label(
            self.root,
            image=self.tc_logo_photo,
            bg="#000000",
        )
        self.tc_logo.image = self.tc_logo_photo  # Keep reference
        self.tc_logo.place(x=240, y=0, width=660, height=200)
        
        # log_in_button
        self.log_in_button = tk.Button(
            self.root,
            text="Log In/Sign Up",
            font=("Arial", 59),
            command=self.on_log_in_button_click
        )
        self.log_in_button.place(x=0, y=820, width=1080, height=220)
        
        # langs_text
        self.langs_text = tk.Label(
            self.root,
            text="Languages",
            fg="#000000",
            font=("Arial", 20),
            anchor="center"
        )
        self.langs_text.place(x=30, y=20, width=120, height=40)
        
        # acces_button
        self.acces_button = tk.Button(
            self.root,
            text="Accessibility",
            font=("Arial", 40),
            command=self.on_acces_button_click
        )
        self.acces_button.place(x=170, y=1050, width=240, height=270)
        
        # zoom_in_button
        self.zoom_in_button = tk.Button(
            self.root,
            text="Zoom Out",
            font=("Arial", 40),
            command=self.on_zoom_in_button_click
        )
        self.zoom_in_button.place(x=730, y=1050, width=240, height=270)
        
        # zoom_out_button
        self.zoom_out_button = tk.Button(
            self.root,
            text="Zoom In",
            font=("Arial", 40),
            command=self.on_zoom_out_button_click
        )
        self.zoom_out_button.place(x=450, y=1050, width=240, height=270)
        
        # search_bar
        self.search_bar = tk.Entry(
            self.root,
            font=("Arial", 31),
            bg="#ffffff",
            fg="#000000"
        )
        self.search_bar.place(x=230, y=210, width=670, height=80)
        self.search_bar.insert(0, "Search...")  # Placeholder text
    
    # ==========================================
    # Event Handlers - Implement your logic here
    # ==========================================
    
    def on_map_button_click(self): 
        self.app.show_mapscreen()
        pass
    
    def on_help_button_click(self):
        """
        Handle on_help_button_click event
        TODO: Implement your logic here
        """
        pass
    
    def on_up_floor_button_click(self):
        """
        Handle on_up_floor_button_click event
        TODO: Implement your logic here
        """
        pass
    
    def on_park_button_click(self):
        """
        Handle on_park_button_click event
        TODO: Implement your logic here
        """
        pass
    
    def on_low_floor_button_click(self):
        self.app.show_foodcourt()
        pass
    
    def on_store_button_click(self):
        self.app.show_searchscreen()
        pass
    
    def on_eng_lang_click(self):
        """
        Handle on_eng_lang_click event
        TODO: Implement your logic here
        """
        pass
    
    def on_dutch_button_click(self):
        """
        Handle on_dutch_button_click event
        TODO: Implement your logic here
        """
        pass
    
    def on_germ_button_click(self):
        """
        Handle on_germ_button_click event
        TODO: Implement your logic here
        """
        pass
    
    def on_french_lang_click(self):
        """
        Handle on_french_lang_click event
        TODO: Implement your logic here
        """
        pass
    
    def on_span_button_click(self):
        """
        Handle on_span_button_click event
        TODO: Implement your logic here
        """
        pass
    
    def on_log_in_button_click(self):
        """
        Handle on_log_in_button_click event
        TODO: Implement your logic here
        """
        pass
    
    def on_acces_button_click(self):
        """
        Handle on_acces_button_click event
        TODO: Implement your logic here
        """
        pass
    
    def on_zoom_in_button_click(self):
        """
        Handle on_zoom_in_button_click event
        TODO: Implement your logic here
        """
        pass
    
    def on_zoom_out_button_click(self):
        """
        Handle on_zoom_out_button_click event
        TODO: Implement your logic here
        """
        pass