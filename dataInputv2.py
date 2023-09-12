import tkinter as tk
    
#Archivos adicionales
import caminosMatriz as cm 
import componentesConexas as cc
import dataInputv2 as dt
    
class dataInput:

    def __init__(self, Screen):
        self.Screen = Screen
       
        #Variables
        #Tamaño matriz
        self.sizeMatrix = tk.StringVar()
        self.sizeMatrix.set("0")
        #Status Matriz
        self.informacionMatriz = tk.StringVar()
        self.informacionMatriz.set("Ingrese la informacion de la matriz")
        #Matriz Data
        self.dataMatrix = []
        #Entries Data
        self.entriesMatrix = []
 
        self.genMatrix()
        self.hideMatrix()
        
        #Tamaño matriz
        #Label
        self.sizeMatrixLabel = tk.Label(self.Screen, text="Tamaño de la matriz:")
        #Entry
        self.sizeMatrixEntry = tk.Entry(self.Screen, textvariable=(self.sizeMatrix))
        
        
        #Status matriz
        #Label
        self.statusMatrix = tk.Label(self.Screen, text = "Status: ")
        self.statusModMatrix = tk.Label(self.Screen, text = "Ingrese la informacion de la matriz", textvariable = self.informacionMatriz)


        #Generar matriz
        #Button
        self.buttonGenerarMatriz = tk.Button(self.Screen, text = "Generar Matriz", width = 15, command = self.generarMatriz)


    def showMatrix(self):
        posX = 240
        posY = 40

        for indexRow in range(int(self.sizeMatrix.get())):
            for indexColumn in range(int(self.sizeMatrix.get())):
                self.entriesMatrix[indexRow][indexColumn].place(x=posX + indexColumn * 20, y=posY + indexRow * 20)


    def hideMatrix(self):
        for indexRow in range(15):
            for indexColumn in range(15):
                self.entriesMatrix[indexRow][indexColumn].place_forget()


    def genMatrix(self):
        posX = 240
        posY = 40

        for indexRow in range(15):
            self.dataMatrix.append([])
            self.entriesMatrix.append([])
            for indexColumn in range(15):
                self.dataMatrix[indexRow].append(tk.StringVar())
                self.entriesMatrix[indexRow].append(
                    tk.Entry(self.Screen, textvariable=self.dataMatrix[indexRow][indexColumn], width=2))
                self.entriesMatrix[indexRow][indexColumn].place(
                    x=posX + indexColumn * 20, y=posY + indexRow * 20)
     

    def show(self):
        #Status matrix
        #Label
        self.statusMatrix.place(x = 20, y = 240)
        self.statusModMatrix.place(x = 20, y = 260)

        #Tamaño matrix
        #Label
        self.sizeMatrixLabel.place(x=20, y=300)
        #Entry
        self.sizeMatrixEntry.place(x=20, y=320)

        #Generar Matriz
        #Button
        self.buttonGenerarMatriz.place(x = 20, y = 340)

        
    def hide(self):
        #Tamaño matrix
        #Label
        self.sizeMatrixLabel.place_forget()
        #Entry
        self.sizeMatrixEntry.place_forget()
        
        #Status matrix
        #Label
        self.statusMatrix.place_forget()
        self.statusModMatrix.place_forget()
    
        #Generar Matriz
        #Button
        self.buttonGenerarMatriz.place_forget()
        self.hideMatrix()
    
    
    def generarMatriz(self):
        if self.verificacionSizeMatrix() == 2:
            self.showMatrix()
    
    
    def verificacionSizeMatrix(self):
        # Output Data
        # 0 El entry tiene 0
        # 1 El entry tiene un dato no valido
        # 2 El entry tiene un dato valido

        sizeMatrixData = self.sizeMatrix.get()
        sizeMatrixData = sizeMatrixData.replace(" ", "")

        if not str(sizeMatrixData).isdigit():
            self.informacionMatriz.set(
                "El valor de la matriz ingresada no es valida. Ingrese el valor entre 5 a 15")
            return 1

        sizeMatrixData = int(sizeMatrixData)
        if sizeMatrixData == 0:
            self.informacionMatriz.set(
                "El valor de la matriz ingresada no es valida. Ingrese el valor entre 5 a 15")
            return 0

        if not (sizeMatrixData >= 5 and sizeMatrixData <= 15):
            self.informacionMatriz.set(
                "El valor de la matriz ingresada no es valida. Ingrese el valor entre 5 a 15")
            return 1

        self.informacionMatriz.set("El valor de la matriz exitoso")
        return 2


#Ingreso de datos
#Aleatorio
#def dataRandom(sizeMatrix):


#Manual
#def dataManual(sizeMatrix):
