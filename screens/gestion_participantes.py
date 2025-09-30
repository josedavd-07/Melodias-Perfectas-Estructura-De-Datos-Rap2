import customtkinter as ctK
from screens.base import ScreenBase
from PIL import Image
from Utils.custom_messagebox import CustomMessageBox
import datetime


class GestionParticipantes(ScreenBase):
    def __init__(self, master):
        super().__init__(master)
        # 💰 Dictionary to store class costs from Table 2
        self.class_costs = {
            "Dibujo": 70000,
            "Pintura": 85000,
            "Escritura": 100000,
            "Fotografía": 90000,
            "Grabado": 75000,
        }

    def show(self):
        # 🎨 Colores
        bg_color = "#2F3A46"
        frame_color = "#3E4A57"
        border_color = "#556272"
        entry_bg = "#E6E1DC"
        entry_text = "#2F3A46"
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
            self, fg_color=frame_color, width=400, height=400,
            corner_radius=0, border_width=3, border_color=border_color
        )
        frame.place(relx=0.5, rely=0.5, anchor="center")
        
        # Configure rows and columns to be responsive
        frame.grid_columnconfigure(0, weight=1)
        frame.grid_columnconfigure(1, weight=1)
        
        # Title Label
        ctK.CTkLabel(frame, text="Registro de Participantes",
                     font=("Segoe UI", 16, "bold"), text_color=label_color).grid(row=0, column=0, columnspan=2, pady=(20, 10))

        # --- Identificación ---
        ctK.CTkLabel(frame, text="Identificación", font=("Segoe UI", 12), text_color=label_color).grid(row=1, column=0, sticky="w", padx=(30, 10), pady=5)
        self.entry_identificacion = ctK.CTkEntry(
            frame, font=("Segoe UI", 14, "bold"), fg_color=entry_bg, text_color=entry_text
        )
        self.entry_identificacion.grid(row=1, column=1, sticky="ew", padx=(10, 30), pady=5)

        # --- Nombre Completo ---
        ctK.CTkLabel(frame, text="Nombre Completo", font=("Segoe UI", 12), text_color=label_color).grid(row=2, column=0, sticky="w", padx=(30, 10), pady=5)
        self.entry_nombre = ctK.CTkEntry(
            frame, font=("Segoe UI", 14, "bold"), fg_color=entry_bg, text_color=entry_text
        )
        self.entry_nombre.grid(row=2, column=1, sticky="ew", padx=(10, 30), pady=5)

        # --- Género ---
        ctK.CTkLabel(frame, text="Género", font=("Segoe UI", 12), text_color=label_color).grid(row=3, column=0, sticky="w", padx=(30, 10), pady=5)
        self.gender_var = ctK.StringVar(value="Masculino")
        radio_frame = ctK.CTkFrame(frame, fg_color="transparent")
        radio_frame.grid(row=3, column=1, sticky="ew", padx=(10, 30), pady=5)
        radio_frame.grid_columnconfigure(0, weight=1)
        radio_frame.grid_columnconfigure(1, weight=1)
        ctK.CTkRadioButton(radio_frame, text="Masculino", variable=self.gender_var, value="Masculino", font=("Segoe UI", 12), text_color=label_color, fg_color=button_color).grid(row=0, column=0, sticky="w")
        ctK.CTkRadioButton(radio_frame, text="Femenino", variable=self.gender_var, value="Femenino", font=("Segoe UI", 12), text_color=label_color, fg_color=button_color).grid(row=0, column=1, sticky="w")

        # --- Técnica Artística ---
        ctK.CTkLabel(frame, text="Técnica Artística", font=("Segoe UI", 12), text_color=label_color).grid(row=4, column=0, sticky="w", padx=(30, 10), pady=5)
        self.combobox_tecnica = ctK.CTkComboBox(
            frame, values=list(self.class_costs.keys()),
            font=("Segoe UI", 14, "bold"),
            fg_color=entry_bg, text_color=entry_text,
            dropdown_fg_color=frame_color, 
            dropdown_text_color="#1D3036", #Color de texto
            command=self._update_cost
)
        self.combobox_tecnica.set("Seleccionar...")
        self.combobox_tecnica.grid(row=4, column=1, sticky="ew", padx=(10, 30), pady=5)

        # --- Costo por Clase ---
        ctK.CTkLabel(frame, text="Costo por Clase", font=("Segoe UI", 12), text_color=label_color).grid(row=5, column=0, sticky="w", padx=(30, 10), pady=5)
        self.entry_costo = ctK.CTkEntry(
            frame, font=("Segoe UI", 14, "bold"), fg_color=entry_bg, text_color=entry_text, state="readonly"
        )
        self.entry_costo.grid(row=5, column=1, sticky="ew", padx=(10, 30), pady=5)

        # --- Número de Clases ---
        ctK.CTkLabel(frame, text="Número de Clases", font=("Segoe UI", 12), text_color=label_color).grid(row=6, column=0, sticky="w", padx=(30, 10), pady=5)
        self.entry_num_clases = ctK.CTkEntry(
            frame, font=("Segoe UI", 14, "bold"), fg_color=entry_bg, text_color=entry_text
        )
        self.entry_num_clases.grid(row=6, column=1, sticky="ew", padx=(10, 30), pady=5)

        # --- Buttons ---
        buttons_frame = ctK.CTkFrame(frame, fg_color="transparent")
        buttons_frame.grid(row=7, column=0, columnspan=2, pady=(20, 10))
        
        ctK.CTkButton(buttons_frame, text="Guardar Registro", width=150,
                      font=("Segoe UI", 14, "bold"),
                      fg_color=button_color, hover_color=button_hover,
                      command=self._save_record, text_color=entry_bg).pack(side="left", padx=5)

        ctK.CTkButton(buttons_frame, text="Calcular Costo / Mostrar Reporte", width=200,
                      font=("Segoe UI", 14, "bold"),
                      fg_color=button_color, hover_color=button_hover,
                      command=self._validate_and_show_report, text_color=entry_bg).pack(side="right", padx=5)
                      
        ctK.CTkButton(frame, text="Salir", width=140,
                      font=("Segoe UI", 14, "bold"),
                      fg_color=button_color, hover_color=button_hover,
                      command=self._exit_app, text_color=entry_bg).grid(row=8, column=0, columnspan=2, pady=(10, 20))


        # Show screen
        self.pack(expand=True, fill="both")

    def _update_cost(self, selection):
        """Updates the cost entry based on the artistic technique selected."""
        cost = self.class_costs.get(selection, 0)
        self.entry_costo.configure(state="normal")
        self.entry_costo.delete(0, ctK.END)
        self.entry_costo.insert(0, f"${cost:,}")
        self.entry_costo.configure(state="readonly")

    def _validate_and_show_report(self):
        """Validates all fields and shows the report screen."""
        try:
            identificacion = self.entry_identificacion.get()
            nombre = self.entry_nombre.get()
            tecnica = self.combobox_tecnica.get()
            num_clases = self.entry_num_clases.get()
            
            if not identificacion or not nombre or not tecnica or not num_clases:
                CustomMessageBox(self, "Error de Datos", "Por favor, complete todos los campos.").wait_window()
                return

            try:
                identificacion = int(identificacion)
                # Fix: Allow spaces in the name. We check if the name is alpha after removing spaces.
                if not isinstance(nombre, str) or not nombre.replace(" ", "").isalpha():
                    CustomMessageBox(self, "Error de Entrada", "El nombre debe contener solo letras y espacios.").wait_window()
                    return
            except ValueError:
                CustomMessageBox(self, "Error de Entrada", "La identificación debe ser un número.").wait_window()
                return

            if tecnica not in self.class_costs:
                CustomMessageBox(self, "Error", "Por favor, seleccione una técnica artística válida.").wait_window()
                return

            num_clases = int(num_clases)
            if num_clases <= 0:
                CustomMessageBox(self, "Error", "El número de clases debe ser un número positivo.").wait_window()
                return

            costo_clase = self.class_costs[tecnica]
            total_costo = costo_clase * num_clases
            
            # Prepare data to pass to the invoice screen
            data = {
                "identificacion": identificacion,
                "nombre": nombre,
                "genero": self.gender_var.get(),
                "tecnica": tecnica,
                "num_clases": num_clases,
                "costo_clase": costo_clase,
                "total_costo": total_costo,
                "fecha_registro": datetime.date.today().strftime("%Y-%m-%d")
            }
            
            self.hide()
            self.master.factura.show(data)
            
        except ValueError:
            CustomMessageBox(self, "Error de Entrada", "Por favor, ingrese un número válido en el campo 'Número de Clases'.").wait_window()

    def _save_record(self):
        """Saves the participant's data and validates the inputs."""
        identificacion = self.entry_identificacion.get()
        nombre = self.entry_nombre.get()
        tecnica = self.combobox_tecnica.get()
        num_clases = self.entry_num_clases.get()

        # Validación de campos
        if not identificacion or not nombre or not tecnica or not num_clases:
            CustomMessageBox(self, "Error de Datos", "Por favor, complete todos los campos.").wait_window()
            return
        
        try:
            identificacion = int(identificacion)
        except ValueError:
            CustomMessageBox(self, "Error de Entrada", "La identificación debe ser un número.").wait_window()
            return

        # Fix: Allow spaces in the name. We check if the name is alpha after removing spaces.
        if not isinstance(nombre, str) or not nombre.replace(" ", "").isalpha():
            CustomMessageBox(self, "Error de Entrada", "El nombre debe contener solo letras y espacios.").wait_window()
            return

        try:
            num_clases = int(num_clases)
        except ValueError:
            CustomMessageBox(self, "Error de Entrada", "El número de clases debe ser un número.").wait_window()
            return

        CustomMessageBox(self, "Registro Guardado", "Los datos del participante han sido guardados con éxito.").wait_window()
        self._clear_fields()

    def _clear_fields(self):
        """Clears all input fields."""
        self.entry_identificacion.delete(0, ctK.END)
        self.entry_nombre.delete(0, ctK.END)
        self.entry_num_clases.delete(0, ctK.END)
        self.gender_var.set("Masculino")
        self.combobox_tecnica.set("Seleccionar...")
        self.entry_costo.configure(state="normal")
        self.entry_costo.delete(0, ctK.END)
        self.entry_costo.configure(state="readonly")

    def _exit_app(self):
        """Closes the application."""
        self.master.destroy()