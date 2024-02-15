import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


'''
nombre: Santiago
apellido: Gomez
---
Ejercicio: Match_02
---
Enunciado:
Al presionar el botón ‘Informar’ mostrar mediante alert los siguientes mensajes 
en función del mes seleccionado:
    Si estamos en invierno: ‘¡Abrígate que hace frío!’
    Si aún no llegó el invierno: ‘Falta para el invierno..’
    Si ya pasó el invierno: ‘¡Ya pasamos frío, ahora calor!’
	
Aclaracion: tomamos a Julio y Agosto como los meses de invierno

'''


class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        self.label_meses = customtkinter.CTkLabel(master=self, text="Meses")
        self.label_meses.grid(row=0, column=0, padx=20, pady=10)
        meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
        self.combobox_mes = customtkinter.CTkComboBox(master=self, values=meses)
        self.combobox_mes.grid(row=1, column=0, padx=20, pady=(10, 10))
        
        self.btn_informar = customtkinter.CTkButton(master=self, text="Informar", command=self.btn_informar_on_click)
        self.btn_informar.grid(row=2, pady=20, columnspan=2, sticky="nsew")
        
    
    def btn_informar_on_click(self):
        mes = self.combobox_mes.get()
        match mes:
            case "Enero":
                mensaje = "falta para el invierno.."
                alert("Mes", mensaje)
            case "Febrero":
                mensaje = "falta para el invierno.."
                alert("Mes", mensaje)
            case "Marzo":
                mensaje = "falta para el invierno.."
                alert("Mes", mensaje)
            case "Abril":
                mensaje = "falta para el invierno.."
                alert("Mes", mensaje)
            case "Mayo":
                mensaje = "falta para el invierno.."
                alert("Mes", mensaje)
            case "Junio":
                mensaje = "falta para el invierno.."
                alert("Mes", mensaje)
            case "Julio":
                mensaje = "¡Abrígate que hace frío!"
                alert("Mes", mensaje)
            case "Agosto":
                mensaje = "¡Abrígate que hace frío!"
                alert("Mes", mensaje)
            case "Septiembre":
                mensaje = "¡Ya pasamos frío, ahora calor!"
                alert("Mes", mensaje)
            case "Octubre":
                mensaje = "¡Ya pasamos frío, ahora calor!"
                alert("Mes", mensaje)
            case "Noviembre":
                mensaje = "¡Ya pasamos frío, ahora calor!"
                alert("Mes", mensaje)
            case "Diciembre":
                mensaje = "¡Ya pasamos frío, ahora calor!"
                alert("Mes", mensaje)    

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()