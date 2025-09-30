import customtkinter as ctK
from screens.base import ScreenBase
from Utils.custom_messagebox import CustomMessageBox
from PIL import Image

class Factura(ScreenBase):
    def __init__(self, master):
        super().__init__(master)

    def show(self, data):
        # 🎨 Colores
        bg_color = "#2F3A46"
        frame_color = "#3E4A57"
        border_color = "#556272"
        label_color = "#C0B9AE"
        button_color = "#556272"
        button_hover = "#7A8899"
        
        # Background
        try:
            bg_image = ctK.CTkImage(Image.open("assets/img/MelodiasPerfectas.png"), size=(650, 450))
            label_bg = ctK.CTkLabel(self, image=bg_image, text="")
            label_bg.place(x=0, y=0, relwidth=1, relheight=1)
        except:
            self.configure(bg=bg_color)

        # Central frame
        frame = ctK.CTkFrame(
            self, fg_color=frame_color, width=400, height=350,
            corner_radius=0, border_width=3, border_color=border_color
        )
        frame.place(relx=0.5, rely=0.5, anchor="center")

        # Title Label
        ctK.CTkLabel(frame, text="Reporte de Costo",
                     font=("Segoe UI", 16, "bold"), text_color=label_color).pack(pady=(20, 10))
        
        # Report details
        report_text = f"Nombre: {data['nombre']}\n"
        report_text += f"ID: {data['identificacion']}\n"
        report_text += f"Género: {data['genero']}\n"
        report_text += f"Técnica: {data['tecnica']}\n"
        report_text += f"Clases: {data['num_clases']}\n"
        report_text += f"Fecha de Registro: {data['fecha_registro']}\n"
        report_text += f"Costo por Clase: ${data['costo_clase']:,}\n"
        report_text += f"Total a Pagar: ${data['total_costo']:,}"
        
        ctK.CTkLabel(frame, text=report_text, font=("Segoe UI", 14), text_color=label_color, justify="left").pack(pady=20, padx=30)
        
        # Aceptar button
        ctK.CTkButton(frame, text="Aceptar", width=140,
                      font=("Segoe UI", 14, "bold"),
                      fg_color=button_color, hover_color=button_hover,
                      command=self._go_back, text_color=label_color).pack(pady=20)

        # Show screen
        self.pack(expand=True, fill="both")
        
    def _go_back(self):
        self.hide()
        self.master.gestion_participantes.show()
