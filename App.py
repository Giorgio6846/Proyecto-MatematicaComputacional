import tkinter as tk 

#Archivos adicionales
import caminosMatriz as cm
import componentesConexas as cc
import dataInputv2 as dt

class App:
          
    def __init__(self, master):
        self.master = master
        
        self.master.title(
            'Proyecto - Matematica Computacional - ( 2023 - 2 ) - Grupo 5 - Seccion SS41')
        
        #Layout
        self.master.geometry("800x600")
        self.master.resizable(False, False)
        self.master.config(background='grey')
        
        #Frames
        #Menu
        menuFrame = tk.Frame(self.master, width = 200, height = 200, bg = 'white')
        menuFrame.place(x = 20, y = 20)

        #SubMenu
        subMenuFrame = tk.Frame(self.master, width = 200, height = 340, bg = 'white')
        subMenuFrame.place(x = 20, y = 240)

        #Vista
        viewFrame = tk.Frame(self.master, width=540, height=560, bg='white')
        viewFrame.place(x = 240, y = 20)
        
        #Opciones de usuario
        buttonData = tk.Button(self.master, text="Ingreso datos", width=15,
                               command=self.dataInputInterface).place(x=30, y=40)
        buttonMatrix = tk.Button(self.master, text="Matriz de Caminos ", width=15,
                                command=self.matrizCaminosInterface).place(x=30, y=40 + 30)
        buttonComponentesConexas = tk.Button(self.master, text="Componentes Conexas", width=15,
                                command=self.componentesConexasInterface).place(x=30, y=40 + 60)
    
        self.interfazEntradaDatos = dt.dataInput(self.master)
        self.interfazComponentesConexas = cc.componentesConexas(self.master)
        self.interfazMatrizCaminos = cm.matrizCaminos(self.master)
   
    #Ingreso datos
    def dataInputInterface(self):
        self.interfazMatrizCaminos.hide()
        self.interfazComponentesConexas.hide()
        self.interfazEntradaDatos.show()

    #Matriz de Caminos
    def matrizCaminosInterface(self):
        if self.interfazEntradaDatos.getVerificacion():
            arrayTMP = self.interfazEntradaDatos.getMatriz()
            sizeMatrix = self.interfazEntradaDatos.getSizeMatrix()
            print(arrayTMP)
            print(sizeMatrix)
            self.interfazMatrizCaminos.setMatrix(arrayTMP, sizeMatrix)
            self.interfazMatrizCaminos.show()        

        self.interfazComponentesConexas.hide()
        self.interfazEntradaDatos.hide()

    #Componentes Conexas
    def componentesConexasInterface(self):
        self.interfazMatrizCaminos.hide()
        self.interfazComponentesConexas.show()
        self.interfazEntradaDatos.hide()

root = tk.Tk()
app = App(root)
root.mainloop()