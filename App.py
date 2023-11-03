import tkinter as tk 

#Archivos adicionales
import caminosMatriz as cm
import componentesConexas as cc
import dataInput as dt
import platform

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
        
        if platform.system() == 'Windows':
            widthButton = 25
        elif platform.system() == 'Darwin':
            widthButton = 17

        #Opciones de usuario
        buttonData = tk.Button(self.master, text="Ingreso datos", width=widthButton,
                                command=self.dataInputInterface).place(x=25, y=40)
        buttonMatrix = tk.Button(self.master, text="Matriz de Caminos ", width=widthButton,
                                    command=self.matrizCaminosInterface).place(x=25, y=40 + 30)
        buttonComponentesConexas = tk.Button(self.master, text="Componentes Conexas", width=widthButton,
                                                command=self.componentesConexasInterface).place(x=25, y=40 + 60)


        self.dataApp = Data()

        self.interfazEntradaDatos = dt.dataInput(self.master,self.dataApp)
        self.interfazComponentesConexas = cc.componentesConexas(self.master,self.dataApp)
        self.interfazMatrizCaminos = cm.matrizCaminos(
            self.master, self.dataApp)
   
   
    #Ingreso datos
    def dataInputInterface(self):
        self.interfazMatrizCaminos.hide()
        self.interfazComponentesConexas.hide()
        self.interfazEntradaDatos.show()

    def testDataApp(self):
        print(self.dataApp.getMatriz())
        print(self.dataApp.getMatrizCaminos())
        print(self.dataApp.getSizeMatrix())

    #Matriz de Caminos
    def matrizCaminosInterface(self):
        if self.interfazEntradaDatos.getVerificacion():
            self.interfazEntradaDatos.getSizeMatrix()
            self.interfazEntradaDatos.getMatrix()
            
            self.testDataApp()
            self.interfazMatrizCaminos.show()        

        self.interfazComponentesConexas.hide()
        self.interfazEntradaDatos.hide()

    #Componentes Conexas
    def componentesConexasInterface(self):
        if self.interfazMatrizCaminos.getCheck():
            self.interfazMatrizCaminos.getMatriz()
             
            self.testDataApp()
            self.interfazMatrizCaminos.clearCheckbox()
            self.interfazComponentesConexas.show()
             
        self.interfazMatrizCaminos.hide()
        self.interfazEntradaDatos.hide()

class Data:
    def __init__(self):
        self.matriz = []
        self.matrizCaminos = []
        self.sizeMatrix = 0
    
    def setSizeMatrix(self, size):
        self.sizeMatrix = size
    
    def setMatrix(self,matrix):
        print(matrix)
        self.matriz = matrix
        
    def setMatrizCaminos(self,matrizCaminos):
        self.matrizCaminos = matrizCaminos
        
    def getSizeMatrix(self):
        return self.sizeMatrix

    def getMatriz(self):
        return self.matriz
    
    def getMatrizCaminos(self):
        return self.matrizCaminos
    
    def clearData(self):
        self.matrix = []
        self.matrizCaminos = []
        self.sizeMatrix = 0
    
root = tk.Tk()
app = App(root)
root.mainloop()