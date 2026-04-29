
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import base64
from io import BytesIO


class mapscreen:
    def __init__(self, root, app):
        self.root = root
        self.app = app
        self.root.title("Map")
        self.root.geometry("1080x1340")
        self.root.resizable(True, True)
        
        # Initialize variables
        
        # Create widgets
        self._create_widgets()
    
    def _create_widgets(self):
        self.frame = tk.Frame(self.root, width = 1080, height = 1340)
        self.frame.place(x=0, y=0)
        
        # map_text
        self.map_text = tk.Label(
            self.root,
            text="Map",
            bg="#ffffff",
            fg="#000000",
            font=("Arial", 50),
            anchor="center"
        )
        self.map_text.place(x=340, y=40, width=340, height=160)
        
        # small_tc_logo
        # Load image for small_tc_logo
        self.small_tc_logo_photo = tk.PhotoImage(file="assets/small_tc_logo.png")
        self.small_tc_logo = tk.Label(
            self.root,
            image=self.small_tc_logo_photo,
        )
        self.small_tc_logo.image = self.small_tc_logo_photo  # Keep reference
        self.small_tc_logo.place(x=20, y=30, width=150, height=150)
        
        # map
        # Load image for map
        self.map_photo = tk.PhotoImage(file="assets/map.png")
        self.map = tk.Label(
            self.root,
            image=self.map_photo,
        )
        self.map.image = self.map_photo  # Keep reference
        self.map.place(x=60, y=320, width=960, height=720)
        
        # back_button_map_page
        self.back_button_map_page = tk.Button(
            self.root,
            text="Back",
            font=("Arial", 25),
            command=self.on_back_button_map_page_click
        )
        self.back_button_map_page.place(x=810, y=60, width=200, height=80)
    
    # ==========================================
    # Event Handlers - Implement your logic here
    # ==========================================
    
    def on_back_button_map_page_click(self):
        self.app.show_home()
        pass
