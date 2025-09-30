import customtkinter as ctK
from PIL import Image
from screens.base import ScreenBase
from Utils.custom_messagebox import CustomMessageBox


class Login(ScreenBase):
    def __init__(self, master):
        super().__init__(master)
        self.password = "123"

    def show(self):
        # 🎨 Paleta de colores
        bg_color = "#2F3A46" 
        frame_color = "#3E4A57" 
        border_color = "#556272" 
        label_color = "#C0B9AE" 
        accent_color = "#7A8899" 
        button_color = "#556272" 
        button_hover = "#7A8899" 
        entry_bg = "#E6E1DC" 
        entry_text = "#2F3A46" 

        # Background
        try:
            bg_image = ctK.CTkImage(Image.open("assets/img/MelodiasPerfectas.png"), size=(650, 450))
            label_bg = ctK.CTkLabel(self, image=bg_image, text="")
            label_bg.place(x=0, y=0, relwidth=1, relheight=1)
        except:
            self.configure(bg=bg_color)

        # Central frame
        frame = ctK.CTkFrame(
            self, fg_color=frame_color, width=360, height=340,
            corner_radius=0, border_width=3, border_color=border_color
        )
        frame.place(relx=0.5, rely=0.5, anchor="center")

        # Labels
        ctK.CTkLabel(frame, text="Jose David Carranza Angarita",
                     font=("Segoe UI", 16, "bold"), text_color=label_color).place(relx=0.5, rely=0.10, anchor="n")

        ctK.CTkLabel(frame, text="🎨 Perfect Melodies 🎶",
                     font=("Segoe UI", 18, "bold"), text_color=accent_color).place(relx=0.5, rely=0.22, anchor="n")

        ctK.CTkLabel(frame, text="Course: Data Structures",
                     font=("Segoe UI", 14), text_color=label_color).place(relx=0.5, rely=0.32, anchor="n")

        # Password
        ctK.CTkLabel(frame, text="Enter the access password:",
                     font=("Segoe UI", 14, "italic"), text_color=label_color).place(relx=0.5, rely=0.46, anchor="n")

        self.entry_password = ctK.CTkEntry(frame, show="*", width=240,
                                         font=("Segoe UI", 14, "bold"),
                                         fg_color=entry_bg, text_color=entry_text)
        self.entry_password.place(relx=0.5, rely=0.54, anchor="n")

        # Button
        ctK.CTkButton(frame, text="Login", width=140,
                      font=("Segoe UI", 14, "bold"),
                      fg_color=button_color, hover_color=button_hover,
                      command=self.validate_password,
                      text_color=entry_bg).place(relx=0.5, rely=0.68, anchor="n")

        self.pack(expand=True, fill="both")

    def check_password(self, value: str) -> bool:
        return value == self.password                       
    def validate_password(self):
        entered = self.entry_password.get().strip()

        if entered == "":
            CustomMessageBox(self, "Access Denied", "Please enter the password")
        elif self.check_password(entered):
            msg = CustomMessageBox(self, "Access Granted", "Correct password!")
            if msg.result == "OK":
                self.go_to_gestion_participantes()
        else:
            CustomMessageBox(self, "Access Denied", "Incorrect password")
            self.entry_password.delete(0, "end")


    def go_to_gestion_participantes(self):
        self.hide()
        self.master.gestion_participantes.show()
