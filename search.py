
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import base64
from io import BytesIO


class searchscreen:
    def __init__(self, root, app):
        self.root = root
        self.app = app
        self.root.title("Search")
        self.root.geometry("1080x1340")
        self.root.resizable(True, True)
        
        # Initialize variables
        
        # Create widgets
        self._create_widgets()
    
    def _create_widgets(self):
        self.frame = tk.Frame(self.root, width = 1080, height = 1340)
        self.frame.place(x=0, y=0)
        
        # small_tc_logo
        # Load image for small_tc_logo
        self.small_tc_logo_photo = tk.PhotoImage(file="assets/small_tc_logo.png")
        self.small_tc_logo = tk.Label(
            self.root,
            image=self.small_tc_logo_photo,
        )
        self.small_tc_logo.image = self.small_tc_logo_photo  # Keep reference
        self.small_tc_logo.place(x=20, y=10, width=150, height=150)
        
        # search_text
        self.search_text = tk.Label(
            self.root,
            text="Search",
            bg="#ffffff",
            fg="#000000",
            font=("Arial", 56),
            anchor="center"
        )
        self.search_text.place(x=200, y=40, width=640, height=120)
        
        # frame_1
        self.frame_1 = tk.Frame(
            self.root,
            bg="#f3f4f6",
            relief="groove",
            bd=1
        )
        self.frame_1.place(x=10, y=320, width=1060, height=590)
        
        # search_bar
        self.search_bar = tk.Entry(
            self.root,
            font=("Arial", 35),
            bg="#ffffff",
            fg="#000000"
        )
        self.search_bar.place(x=10, y=170, width=1060, height=130)
        self.search_bar.insert(0, "")  # Placeholder text
        
        
        # q_button
        self.q_button = tk.Button(
            self.root,
            text="Q",
            font=("Arial", 30),
            command=self.on_q_button_click
        )
        self.q_button.place(x=30, y=450, width=90, height=110)
        
        # spacebar
        self.spacebar = tk.Button(
            self.root,
            text="Space ",
            font=("Arial", 30),
            command=self.on_spacebar_click
        )
        self.spacebar.place(x=180, y=820, width=690, height=80)
        
        # l_button
        self.l_button = tk.Button(
            self.root,
            text="L",
            font=("Arial", 30),
            command=self.on_l_button_click
        )
        self.l_button.place(x=870, y=570, width=90, height=110)
        
        # m_button
        self.m_button = tk.Button(
            self.root,
            text="M",
            font=("Arial", 30),
            command=self.on_m_button_click
        )
        self.m_button.place(x=760, y=690, width=90, height=110)
        
        # n_button
        self.n_button = tk.Button(
            self.root,
            text="N",
            font=("Arial", 30),
            command=self.on_n_button_click
        )
        self.n_button.place(x=660, y=690, width=90, height=110)
        
        # b_button
        self.b_button = tk.Button(
            self.root,
            text="B",
            font=("Arial", 30),
            command=self.on_b_button_click
        )
        self.b_button.place(x=560, y=690, width=90, height=110)
        
        # v_button
        self.v_button = tk.Button(
            self.root,
            text="V",
            font=("Arial", 30),
            command=self.on_v_button_click
        )
        self.v_button.place(x=460, y=690, width=90, height=110)
        
        # c_button
        self.c_button = tk.Button(
            self.root,
            text="C",
            font=("Arial", 30),
            command=self.on_c_button_click
        )
        self.c_button.place(x=360, y=690, width=90, height=110)
        
        # k_button
        self.k_button = tk.Button(
            self.root,
            text="K",
            font=("Arial", 30),
            command=self.on_k_button_click
        )
        self.k_button.place(x=770, y=570, width=90, height=110)
        
        # x_button
        self.x_button = tk.Button(
            self.root,
            text="X",
            font=("Arial", 30),
            command=self.on_x_button_click
        )
        self.x_button.place(x=260, y=690, width=90, height=110)
        
        # z_button
        self.z_button = tk.Button(
            self.root,
            text="Z",
            font=("Arial", 30),
            command=self.on_z_button_click
        )
        self.z_button.place(x=160, y=690, width=90, height=110)
        
        # j_button
        self.j_button = tk.Button(
            self.root,
            text="J",
            font=("Arial", 30),
            command=self.on_j_button_click
        )
        self.j_button.place(x=670, y=570, width=90, height=110)
        
        # h_button
        self.h_button = tk.Button(
            self.root,
            text="H",
            font=("Arial", 30),
            command=self.on_h_button_click
        )
        self.h_button.place(x=570, y=570, width=90, height=110)
        
        # g_button
        self.g_button = tk.Button(
            self.root,
            text="G",
            font=("Arial", 30),
            command=self.on_g_button_click
        )
        self.g_button.place(x=470, y=570, width=90, height=110)
        
        # f_button
        self.f_button = tk.Button(
            self.root,
            text="F",
            font=("Arial", 30),
            command=self.on_f_button_click
        )
        self.f_button.place(x=370, y=570, width=90, height=110)
        
        # d_button
        self.d_button = tk.Button(
            self.root,
            text="D",
            font=("Arial", 30),
            command=self.on_d_button_click
        )
        self.d_button.place(x=270, y=570, width=90, height=110)
        
        # s_button
        self.s_button = tk.Button(
            self.root,
            text="S",
            font=("Arial", 30),
            command=self.on_s_button_click
        )
        self.s_button.place(x=170, y=570, width=90, height=110)
        
        # a_button
        self.a_button = tk.Button(
            self.root,
            text="A",
            font=("Arial", 30),
            command=self.on_a_button_click
        )
        self.a_button.place(x=70, y=570, width=90, height=110)
        
        # o_button
        self.o_button = tk.Button(
            self.root,
            text="O",
            font=("Arial", 30),
            command=self.on_o_button_click
        )
        self.o_button.place(x=830, y=450, width=90, height=110)
        
        # i_button
        self.i_button = tk.Button(
            self.root,
            text="I",
            font=("Arial", 30),
            command=self.on_i_button_click
        )
        self.i_button.place(x=730, y=450, width=90, height=110)
        
        # u_button
        self.u_button = tk.Button(
            self.root,
            text="U",
            font=("Arial", 30),
            command=self.on_u_button_click
        )
        self.u_button.place(x=630, y=450, width=90, height=110)
        
        # y_button
        self.y_button = tk.Button(
            self.root,
            text="Y",
            font=("Arial", 30),
            command=self.on_y_button_click
        )
        self.y_button.place(x=530, y=450, width=90, height=110)
        
        # t_button
        self.t_button = tk.Button(
            self.root,
            text="T",
            font=("Arial", 30),
            command=self.on_t_button_click
        )
        self.t_button.place(x=430, y=450, width=90, height=110)
        
        # r_button
        self.r_button = tk.Button(
            self.root,
            text="R",
            font=("Arial", 30),
            command=self.on_r_button_click
        )
        self.r_button.place(x=330, y=450, width=90, height=110)
        
        # e_button
        self.e_button = tk.Button(
            self.root,
            text="E",
            font=("Arial", 30),
            command=self.on_e_button_click
        )
        self.e_button.place(x=230, y=450, width=90, height=110)
        
        # w_button
        self.w_button = tk.Button(
            self.root,
            text="W",
            font=("Arial", 30),
            command=self.on_w_button_click
        )
        self.w_button.place(x=130, y=450, width=90, height=110)
        
        # p_button
        self.p_button = tk.Button(
            self.root,
            text="P",
            font=("Arial", 30),
            command=self.on_p_button_click
        )
        self.p_button.place(x=930, y=450, width=90, height=110)
        
        # search_button
        self.search_button = tk.Button(
            self.root,
            text="Search",
            font=("Arial", 30),
            command=self.on_search_button_click
        )
        self.search_button.place(x=860, y=690, width=200, height=110)
        
        # numbers_button
        self.numbers_button = tk.Button(
            self.root,
            text="123",
            font=("Arial", 30),
            command=self.on_numbers_button_click
        )
        self.numbers_button.place(x=970, y=570, width=90, height=110)
        
        # backspace
        self.backspace = tk.Button(
            self.root,
            text="Backspace",
            font=("Arial", 36),
            command=self.on_backspace_click
        )
        self.backspace.place(x=840, y=330, width=220, height=110)

        # back_button
        self.back_button = tk.Button(
            self.root,
            text="Back",
            font=("Arial", 36),
            command=self.on_back_button_click
        )
        self.back_button.place(x=870, y=20, width=170, height=120)
        
        # keyboard_languages
        self.keyboard_languages = tk.Button(
            self.root,
            text="Languages",
            font=("Arial", 36),
            command=self.on_keyboard_languages_click
        )
        self.keyboard_languages.place(x=220, y=330, width=580, height=110)
    
    # ==========================================
    # Event Handlers - Implement your logic here
    # ==========================================
    def on_key_click(self, character):
        if character == "Backspace":
            current_text = search_bar.get()
            self.search_bar.delete(0, tk.END)
            self.search_bar.insert(1, current_text[:-1])
        else:
            self.search_bar.insert(tk.END, character)

    
    def on_q_button_click(self):
        self.on_key_click("q")
        pass
    
    def on_spacebar_click(self):
        self.on_key_click(" ")
        pass
    
    def on_l_button_click(self):
        self.on_key_click("l")
        pass
    
    def on_m_button_click(self):
        self.on_key_click("m")
        pass
    
    def on_n_button_click(self):
        self.on_key_click("n")
        pass
    
    def on_b_button_click(self):
        self.on_key_click("b")
        pass
    
    def on_v_button_click(self):
        self.on_key_click("v")
        pass
    
    def on_c_button_click(self):
        self.on_key_click("c")
        pass
    
    def on_k_button_click(self):
        self.on_key_click("k")
        pass
    
    def on_x_button_click(self):
        self.on_key_click("x")
        pass
    
    def on_z_button_click(self):
        self.on_key_click("z")
        pass
    
    def on_j_button_click(self):
        self.on_key_click("j")
        pass
    
    def on_h_button_click(self):
        self.on_key_click("h")
        pass
    
    def on_g_button_click(self):
        self.on_key_click("g")
        pass
    
    def on_f_button_click(self):
        self.on_key_click("f")
        pass
    
    def on_d_button_click(self):
        self.on_key_click("d")
        pass
    
    def on_s_button_click(self):
        self.on_key_click("s")
        pass
    
    def on_a_button_click(self):
        self.on_key_click("a")
        pass
    
    def on_o_button_click(self):
        self.on_key_click("o")
        pass
    
    def on_i_button_click(self):
        self.on_key_click("i")
        pass
    
    def on_u_button_click(self):
        self.on_key_click("u")
        pass
    
    def on_y_button_click(self):
        self.on_key_click("y")
        pass
    
    def on_t_button_click(self):
        self.on_key_click("t")
        pass
    
    def on_r_button_click(self):
        self.on_key_click("r")
        pass
    
    def on_e_button_click(self):
        self.on_key_click("e")
        pass
    
    def on_w_button_click(self):
        self.on_key_click("w")
        pass
    
    def on_p_button_click(self):
        self.on_key_click("p")
        pass
    
    def on_search_button_click(self):
        self.on_confirm_click()
        pass
    
    def on_numbers_button_click(self):
        """
        Handle on_numbers_button_click event
        TODO: Implement your logic here
        """
        pass
    
    def on_backspace_click(self):
        self.on_key_click("Backspace")
        pass

    def on_back_button_click(self):
        self.app.show_home()
        pass
    
    def on_keyboard_languages_click(self):
        """
        Handle on_keyboard_languages_click event
        TODO: Implement your logic here
        """
        pass
    