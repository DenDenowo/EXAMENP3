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
                
    def consultarMateriales(self):
        try:
            conx = self.conexionBD()
            cursor = conx.cursor()
            selectQry = "SELECT * FROM MatConstruccion"
            cursor.execute(selectQry)
            rsMateriales = cursor.fetchall()
            return rsMateriales
        
        except sqlite3.OperationalError:
            messagebox.showinfo("Cuidado", "No se encontraron registros")
    
    def eliminarMaterial(self, id):
        try:
            if(id==""):
                messagebox.showinfo("Cuidado", "ID vacío")
            else:
                if messagebox.askyesno("Eliminar", "¿Está seguro de eliminar el registro con el ID: "+id+"?"):
                    conx = self.conexionBD()
                    cursor = conx.cursor()
                    deleteQry = "DELETE FROM MatConstruccion WHERE IDMat="+id
                    cursor.execute(deleteQry)
                    conx.commit()
                    conx.close()
                    messagebox.showinfo("Información", "Registro eliminado")
                else:
                    messagebox.showinfo("Información", "Operación cancelada")
        except sqlite3.OperationalError:
                messagebox.showinfo("Cuidado", "No se encontró el registro")
                
    def actualizarMaterial(self, id, mat, can):
        if(id == "" or mat == "" or can == ""):
            messagebox.showinfo("Cuidado", "Todos los campos son obligatorios")
        else:
            try:
                if messagebox.askyesno("Actualizar", "¿Está seguro de actualizar el registro con el ID: "+id+"?"):
                    conx = self.conexionBD()
                    cursor = conx.cursor()
                    datos = (mat, can, id)
                    updateQry = "UPDATE MatConstruccion SET Material=?, Cantidad=? WHERE IDMat=?"
                    cursor.execute(updateQry, datos)
                    conx.commit()
                    conx.close()
                    messagebox.showinfo("Información", "Registro actualizado")
                else:
                    messagebox.showinfo("Información", "Operación cancelada")
            except sqlite3.OperationalError:
                messagebox.showinfo("Cuidado", "No se encontró el registro")