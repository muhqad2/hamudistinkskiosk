
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import base64
from io import BytesIO


class lowerfoodcourt:
    def __init__(self, root, app):
        self.root = root
        self.root.title("Lower Food Court")
        self.app = app
        self.root.geometry("1080x1340")
        self.root.resizable(True, True)
        
        # Initialize variables
        
        # Create widgets
        self._create_widgets()
    
    def _create_widgets(self):
        self.frame = tk.Frame(self.root, width = 1080, height = 1340)
        self.frame.place(x=0, y=0)

        # lower_food_court_text
        self.lower_food_court_text = tk.Label(
            self.root,
            text="Lower Food Court",
            bg="#000000",
            fg="#ffffff",
            font=("Arial", 50),
            anchor="center"
        )
        self.lower_food_court_text.place(x=270, y=30, width=540, height=130)
        
        # small_tc_logo
        # Load image for small_tc_logo
        self.small_tc_logo_photo = tk.PhotoImage(file="assets/small_tc_logo.png")
        self.small_tc_logo = tk.Label(
            self.root,
            image=self.small_tc_logo_photo,
        )
        self.small_tc_logo.image = self.small_tc_logo_photo  # Keep reference
        self.small_tc_logo.place(x=10, y=10, width=150, height=150)
        
        # mcdonalds_button
        self.mcdonalds_button = tk.Button(
            self.root,
            text="McDonald's",
            bg="#da291c",
            fg="#ffc72c",
            font=("Verdana", 36),
            command=self.on_mcdonalds_button_click
        )
        self.mcdonalds_button.place(x=190, y=250, width=340, height=80)
        
        # languages_dropdown
        self.languages_dropdown = tk.Button(
            self.root,
            text="Languages",
            font=("Arial", 12),
            command=self.on_languages_dropdown_click
        )
        self.languages_dropdown.place(x=10, y=170, width=150, height=90)

        # back_button
        self.back_button = tk.Button(
            self.root,
            text="Back",
            font=("Arial", 36),
            command=self.on_back_button_click
        )
        self.back_button.place(x=870, y=30, width=150, height=90)
        
        # hop_button
        self.hop_button = tk.Button(
            self.root,
            text="HOP",
            bg="#e2271b",
            font=("Arial", 39),
            command=self.on_hop_button_click
        )
        self.hop_button.place(x=190, y=580, width=340, height=80)
        
        # chopstix_button
        self.chopstix_button = tk.Button(
            self.root,
            text="Chopstix",
            bg="#FE2D2D",
            font=("Courier New", 36),
            command=self.on_chopstix_button_click
        )
        self.chopstix_button.place(x=560, y=360, width=340, height=80)
        
        # barburrito_button
        self.barburrito_button = tk.Button(
            self.root,
            text="Barburrito",
            bg="#FF0000",
            fg="#000000",
            font=("Helvetica", 37),
            command=self.on_barburrito_button_click
        )
        self.barburrito_button.place(x=560, y=470, width=340, height=80)
        
        # wingstop_button
        self.wingstop_button = tk.Button(
            self.root,
            text="Wingstop",
            bg="#146A34",
            fg="#000000",
            font=("Arial", 35),
            command=self.on_wingstop_button_click
        )
        self.wingstop_button.place(x=190, y=470, width=340, height=80)
        
        # burger_king_button
        self.burger_king_button = tk.Button(
            self.root,
            text="Burger King",
            bg="#Ff8732",
            fg="#502314",
            font=("Arial", 37),
            command=self.on_burger_king_button_click
        )
        self.burger_king_button.place(x=190, y=360, width=340, height=80)
        
        # kfc_button
        self.kfc_button = tk.Button(
            self.root,
            text="KFC",
            bg="#ea0029",
            fg="#000000",
            font=("Verdana", 34),
            command=self.on_kfc_button_click
        )
        self.kfc_button.place(x=560, y=250, width=340, height=80)
        
        # jerk_junction_button
        self.jerk_junction_button = tk.Button(
            self.root,
            text="Jerk Junction",
            bg="#89ba43",
            fg="#000000",
            font=("Arial", 38),
            command=self.on_jerk_junction_button_click
        )
        self.jerk_junction_button.place(x=560, y=580, width=340, height=80)
        
        # buttons
        self.buttons = tk.Frame(
            self.root,
            bg="#f3f4f6",
            relief="groove",
            bd=1
        )
        self.buttons.place(x=180, y=210, width=740, height=930)
        self.frame.lower()
        
        # chaiwalla_button
        self.chaiwalla_button = tk.Button(
            self.root,
            text="Chaiwalla",
            bg="#ffffff",
            fg="#000000",
            font=("Arial", 36),
            command=self.on_chaiwalla_button_click
        )
        self.chaiwalla_button.place(x=560, y=910, width=340, height=80)
        
        # millies_button
        self.millies_button = tk.Button(
            self.root,
            text="Millie's Cookies",
            bg="#f11880",
            font=("Courier New", 33),
            command=self.on_millies_button_click
        )
        self.millies_button.place(x=190, y=910, width=340, height=80)
        
        # shake_shack_button
        self.shake_shack_button = tk.Button(
            self.root,
            text="Shake Shack",
            bg="#6ea273",
            fg="#000000",
            font=("Verdana", 34),
            command=self.on_shake_shack_button_click
        )
        self.shake_shack_button.place(x=560, y=800, width=340, height=80)
        
        # east_street_button
        self.east_street_button = tk.Button(
            self.root,
            text="East Street",
            bg="#e3b700",
            fg="#214376",
            font=("Courier New", 39),
            command=self.on_east_street_button_click
        )
        self.east_street_button.place(x=190, y=800, width=340, height=80)
        
        # pizza_hut
        self.pizza_hut = tk.Button(
            self.root,
            text="Pizza Hut",
            bg="#c20f2d",
            font=("Times New Roman", 36),
            command=self.on_pizza_hut_click
        )
        self.pizza_hut.place(x=560, y=690, width=340, height=80)
        
        # nandos_button
        self.nandos_button = tk.Button(
            self.root,
            text="Nando's",
            bg="#000000",
            fg="#D1011B ",
            font=("Verdana", 38),
            command=self.on_nandos_button_click
        )
        self.nandos_button.place(x=190, y=690, width=340, height=80)
        
        # upper_food_court_button
        self.upper_food_court_button = tk.Button(
            self.root,
            text="Upper Food Court",
            font=("Arial", 39),
            command=self.on_upper_food_court_button_click
        )
        self.upper_food_court_button.place(x=210, y=1010, width=640, height=100)
        
        # zoom_buttons
        self.zoom_buttons = tk.Frame(
            self.root,
            bg="#f3f4f6",
            relief="groove",
            bd=1
        )
        self.zoom_buttons.place(x=50, y=1100, width=980, height=220)
        
        # cark_park_2
        self.cark_park_2 = tk.Button(
            self.root,
            text="Car Parking",
            font=("Arial", 34),
            command=self.on_cark_park_2_click
        )
        self.cark_park_2.place(x=220, y=1140, width=250, height=160)
        
        # main_menu_2
        self.main_menu_2 = tk.Button(
            self.root,
            text="Main Menu",
            font=("Arial", 34),
            command=self.on_main_menu_2_click
        )
        self.main_menu_2.place(x=590, y=1140, width=250, height=160)
        
        # settings
        self.settings = tk.Frame(
            self.root,
            bg="#f3f4f6",
            relief="groove",
            bd=1
        )
        self.settings.place(x=920, y=130, width=160, height=340)
        
        # zoom_in_2
        self.zoom_in_2 = tk.Button(
            self.root,
            text="Zoom In",
            font=("Arial", 30),
            command=self.on_zoom_in_2_click
        )
        self.zoom_in_2.place(x=930, y=140, width=140, height=150)
        
        # zoom_out_2
        self.zoom_out_2 = tk.Button(
            self.root,
            text="Zoom Out",
            font=("Arial", 30),
            command=self.on_zoom_out_2_click
        )
        self.zoom_out_2.place(x=930, y=310, width=140, height=150)
    
    # ==========================================
    # Event Handlers - Implement your logic here
    # ==========================================
    
    def on_mcdonalds_button_click(self):
        """
        Handle on_mcdonalds_button_click event
        TODO: Implement your logic here
        """
        pass
    
    def on_languages_dropdown_click(self):
        """
        Handle on_languages_dropdown_click event
        TODO: Implement your logic here
        """
        pass
    
    def on_back_button_click(self):
        self.app.show_home()
        pass
    
    def on_hop_button_click(self):
        """
        Handle on_hop_button_click event
        TODO: Implement your logic here
        """
        pass
    
    def on_chopstix_button_click(self):
        """
        Handle on_chopstix_button_click event
        TODO: Implement your logic here
        """
        pass
    
    def on_barburrito_button_click(self):
        """
        Handle on_barburrito_button_click event
        TODO: Implement your logic here
        """
        pass
    
    def on_wingstop_button_click(self):
        """
        Handle on_wingstop_button_click event
        TODO: Implement your logic here
        """
        pass
    
    def on_burger_king_button_click(self):
        """
        Handle on_burger_king_button_click event
        TODO: Implement your logic here
        """
        pass
    
    def on_kfc_button_click(self):
        """
        Handle on_kfc_button_click event
        TODO: Implement your logic here
        """
        pass
    
    def on_jerk_junction_button_click(self):
        """
        Handle on_jerk_junction_button_click event
        TODO: Implement your logic here
        """
        pass
    
    def on_chaiwalla_button_click(self):
        """
        Handle on_chaiwalla_button_click event
        TODO: Implement your logic here
        """
        pass
    
    def on_millies_button_click(self):
        """
        Handle on_millies_button_click event
        TODO: Implement your logic here
        """
        pass
    
    def on_shake_shack_button_click(self):
        """
        Handle on_shake_shack_button_click event
        TODO: Implement your logic here
        """
        pass
    
    def on_east_street_button_click(self):
        """
        Handle on_east_street_button_click event
        TODO: Implement your logic here
        """
        pass
    
    def on_pizza_hut_click(self):
        """
        Handle on_pizza_hut_click event
        TODO: Implement your logic here
        """
        pass
    
    def on_nandos_button_click(self):
        """
        Handle on_nandos_button_click event
        TODO: Implement your logic here
        """
        pass
    
    def on_upper_food_court_button_click(self):
        """
        Handle on_upper_food_court_button_click event
        TODO: Implement your logic here
        """
        pass
    
    def on_cark_park_2_click(self):
        """
        Handle on_cark_park_2_click event
        TODO: Implement your logic here
        """
        pass
    
    def on_main_menu_2_click(self):
        """
        Handle on_main_menu_2_click event
        TODO: Implement your logic here
        """
        pass
    
    def on_zoom_in_2_click(self):
        """
        Handle on_zoom_in_2_click event
        TODO: Implement your logic here
        """
        pass
    
    def on_zoom_out_2_click(self):
        """
        Handle on_zoom_out_2_click event
        TODO: Implement your logic here
        """
        pass