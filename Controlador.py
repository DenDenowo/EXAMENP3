from tkinter import messagebox
import sqlite3
import bcrypt

class controladorBD:
    def __init__(self):
        pass
    def conexionBD(self):
        try:
            conexion = sqlite3.connect("C:/Users/Deni/Documents/GitHub/EXAMENP3/Ferreteria.db")
            print("Conexión exitosa")
            return conexion
        except sqlite3.OperationalError:
            print("Error al conectar")
        return conexion
    
    def guardarMateriales(self, mat, can):
        conx = self.conexionBD()
        if(mat== "" or can==""):
            messagebox.showwarning("Advertencia", "Todos los campos son obligatorios")
        else:
            cursor = conx.cursor()
            datos = (mat, can)
            qrInsert = "INSERT INTO MatConstruccion(Material, Cantidad) VALUES(?,?)"
            cursor.execute(qrInsert, datos)
            conx.commit()
            conx.close()
            messagebox.showinfo("Información", "Registro exitoso")