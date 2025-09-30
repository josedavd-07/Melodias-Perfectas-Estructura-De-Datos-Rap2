from abc import ABC, abstractmethod
import customtkinter as ctK

class ScreenBase(ctK.CTkFrame, ABC):
    def __init__(self, master):
        super().__init__(master)
        self.master = master 

    @abstractmethod
    def show(self):
        """Cada pantalla debe implementar como mostrarse, con soporte para datos."""
        pass

    def hide(self):
        """Metodo comun para ocultar una pantalla"""
        self.pack_forget()
