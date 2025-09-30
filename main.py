import customtkinter as ctK
from screens.login import Login
from screens.factura import Factura
from screens.gestion_participantes import GestionParticipantes
from screens.base import ScreenBase

class MainApp(ctK.CTk):
    def __init__(self):
        super().__init__()
        self.title("🎶 Melodías Perfectas - Gestión de Participantes")
        self.geometry("650x450")
        self.center_window(650, 450)
        self.resizable(False, False)

        # Pantallas
        self.login = Login(self)
        self.gestion_participantes = GestionParticipantes(self)
        self.factura = Factura(self)

        # Inicia en Login
        self.login.show()

    def center_window(self, width, height):
        """Centrar la ventana principal en la pantalla"""
        self.update_idletasks()
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry(f"{width}x{height}+{x}+{y}")


if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
