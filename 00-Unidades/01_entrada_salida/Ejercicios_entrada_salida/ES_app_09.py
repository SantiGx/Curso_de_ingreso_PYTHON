import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Santiago
apellido: Gomez
---
Ejercicio: entrada_salida_09
---
Enunciado:
Al presionar el botón 'Calcular', se deberá obtener el valor contenido en la caja de texto (txtSueldo), 
transformarlo a número y mostrar el importe de sueldo actualizado con el incremento del 15% utilizando el Dialog Alert.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.label1 = customtkinter.CTkLabel(master=self, text="Sueldo")
        self.label1.grid(row=0, column=0, padx=20, pady=10)
        
        self.txt_sueldo = customtkinter.CTkEntry(master=self)
        self.txt_sueldo.grid(row=0, column=1)
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        sueldo = self.txt_sueldo.get()
        sueldo = float(sueldo)

        calculo1 = (sueldo) * 15
        calculo2 = calculo1 // 100
        calculo3 = sueldo + calculo2
        Mensaje  = f"El sueldo actualizado de {sueldo} más el incremento del 15% es: "
        alert("Sueldo actualizado", Mensaje + str(calculo3))
        #alert("Sueldo Total" , f"El sueldo actualizado de {sueldo} más el incremento del 15% es: {sueldo_act}")


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()