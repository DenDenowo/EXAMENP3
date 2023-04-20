from tkinter import *
from tkinter import ttk
import tkinter as tk
from Controlador import *

controlador = controladorBD()

def ejecutarInsert():
    controlador.guardarMateriales(varMaterial.get(), varCantidad.get())
    varMaterial.set("")
    varCantidad.set("")
        
def limpiarTreeview(tree):
    x = tree.get_children()
    if x != '()':
        tree.delete(*x)
        
def mostrarMateriales():
    limpiarTreeview(txtConsulta)
    materiales = controlador.consultaGeneral()
    for mat in materiales:
        cadena = str(mat[0]) + " " + str(mat[1]) + " " + str(mat[2])
        print(cadena)
        treeMateriales.insert("", "end", values=(mat[0], mat[1], mat[2]))  


Ventana = Tk()
Ventana.title("Ferreteria")
Ventana.geometry("830x390")
Ventana.resizable(0,0)
panel = ttk.Notebook(Ventana)
panel.pack(fill="both", expand="yes")


pestana1 = ttk.Frame(panel)
pestana2 = ttk.Frame(panel)
pestana3 = ttk.Frame(panel)
pestana4 = ttk.Frame(panel)
panel.add(pestana1, text="Insertar Material")
panel.add(pestana2, text="Actualizar Material")
panel.add(pestana3, text="Mostrar Materiales")

#Pestaña 1 Insertar Materiales
titulo = Label(pestana1, text="Registro de Materiales", font=("Helvetica bold", 18), fg="orange").place(x=310, y=10)
lblMaterial = Label(pestana1, text="Material: ", font=("Helvetica bold", 12)).place(x=390, y=50) 
lblCantidad = Label(pestana1, text="Cantidad: ", font=("Helvetica bold", 12)).place(x=390, y=110)
varMaterial = StringVar()
varCantidad = IntVar()
txtMaterial = Entry(pestana1, textvariable=varMaterial, width=30).place(x=330, y=70)
txtCantidad = Entry(pestana1, textvariable=varCantidad, width=30).place(x=330, y=130)
#Boton Insertar centrado y de color naranja oscuro
btnInsertar = Button(pestana1, text="Insertar", command=ejecutarInsert, bg="dark orange", font=("Helvetica bold", 12), fg="white").place(x=390, y=180)

#Pestaña 2 Actualizar Materiales
titulo = Label(pestana2, text="Actualizar Materiales", font=("Helvetica bold", 18), fg="orange").place(x=310, y=10)
lblIdActu = Label(pestana2, text="Id: ", font=("Helvetica bold", 12)).place(x=410, y=50)
lblNombreActu = Label(pestana2, text="Nombre: ", font=("Helvetica bold", 12)).place(x=390, y=110)
lblCantidadActu = Label(pestana2, text="Cantidad: ", font=("Helvetica bold", 12)).place(x=390, y=170)
varIdActu = StringVar()
varNombreActu = StringVar()
varMaterialActu = StringVar()
txtIdActu = Entry(pestana2, textvariable=varIdActu, width=30).place(x=330, y=70)
txtNombreActu = Entry(pestana2, textvariable=varNombreActu, width=30).place(x=330, y=130)
txtMaterialActu = Entry(pestana2, textvariable=varMaterialActu, width=30).place(x=330, y=190)

#botones eliminar y actualizar centrados y de color naranja oscuro
btnEliminar = Button(pestana2, text="Eliminar", command=ejecutarDelete, bg="dark orange", font=("Helvetica bold", 12), fg="white").place(x=390, y=230)
btnActualizar = Button(pestana2, text="Actualizar", command=ejecutarUpdate, bg="dark orange", font=("Helvetica bold", 12), fg="white").place(x=385, y=270)

#Pestaña 3 Mostrar Materiales
titulo = Label(pestana3, text="Materiales", font=("Helvetica bold", 18), fg="orange").place(x=390, y=10)
txtConsulta = ttk.Treeview(pestana3, height=10, columns=("#0", "#1", "#2"))
txtConsulta.place(x=10, y=50)
txtConsulta.heading("#0", text="Id")
txtConsulta.heading("#1", text="Material")
txtConsulta.heading("#2", text="Cantidad")

btnActualizar = Button(pestana3, text="Mostrar Materiales", command=mostrarMateriales, bg="dark orange", font=("Helvetica bold", 12), fg="white").place(x=350, y=300)


Ventana.mainloop()