import customtkinter as ctK

class CustomMessageBox(ctK.CTkToplevel):
    def __init__(self, parent, title, message):
        super().__init__(parent)

        # 🎨 Paleta
        bg_color = "#2F3A46"
        text_color = "#C0B9AE"
        button_color = "#556272"
        button_hover = "#7A8899"
        border_color = "#7A8899"

        # 🎨 Fuentes
        title_font = ("Segoe UI", 16, "bold")
        msg_font = ("Segoe UI", 14)
        btn_font = ("Segoe UI", 13, "bold")

        # Config ventana
        self.configure(fg_color=bg_color)
        self.geometry("360x200")
        self.resizable(False, False)
        self.overrideredirect(True) 

        # 👉 Eventos para arrastrar la ventana
        self.bind("<Button-1>", self.start_move)
        self.bind("<B1-Motion>", self.on_move)

        # Marco
        frame = ctK.CTkFrame(
            self, fg_color=bg_color,
            border_width=2, border_color=border_color,
            corner_radius=12
        )
        frame.pack(expand=True, fill="both", padx=10, pady=10)

        # Barra superior con título
        top_bar = ctK.CTkFrame(frame, fg_color=bg_color, height=30, corner_radius=12)
        top_bar.pack(fill="x", pady=(0, 5))
        top_bar.pack_propagate(False)

        ctK.CTkLabel(top_bar, text=title, font=title_font, text_color=text_color).pack(side="left", padx=10)

        ctK.CTkButton(
            top_bar, text="✖", width=30, fg_color=button_color,
            hover_color=button_hover, text_color=text_color,
            font=("Segoe UI", 12, "bold"), command=self.destroy
        ).pack(side="right", padx=5)

        # Mensaje
        ctK.CTkLabel(
            frame, text=message, font=msg_font,
            text_color=text_color, wraplength=300, justify="center"
        ).pack(pady=(10, 15))

        # Botón OK
        self.result = None
        def confirm():
            self.result = "OK"
            self.destroy()

        ctK.CTkButton(
            frame, text="OK", font=btn_font,
            fg_color=button_color, hover_color=button_hover,
            text_color=text_color, command=confirm, width=100
        ).pack(pady=(0, 10))

        # Centrar
        self.update_idletasks()
        x = self.winfo_screenwidth() // 2 - self.winfo_width() // 2
        y = self.winfo_screenheight() // 2 - self.winfo_height() // 2
        self.geometry(f"+{x}+{y}")

        self.grab_set()
        self.wait_window()

    # --- Métodos para mover la ventana ---
    def start_move(self, event):
        self._x = event.x
        self._y = event.y

    def on_move(self, event):
        x = event.x_root - self._x
        y = event.y_root - self._y
        self.geometry(f"+{x}+{y}")
