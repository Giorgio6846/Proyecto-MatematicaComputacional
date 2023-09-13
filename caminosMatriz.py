import tkinter as tk
import numpy as np

class matrizCaminos:
    global mainWindow

    def __init__(self, Screen):
        #Frame tkinter
        self.Screen = Screen
        
        #Variables
        #Datos Matriz
        self.matrix = np.array([])
        #Tamaño Matriz
        self.sizeMatrix = 0        

        #Label data           
        self.labelMatrix = []
        #Data Matrix 
        self.dataMatrix = []

        self.data = []

        #Pasos de la matriz de caminos
        self.matrizCaminos = []
        
        #Datos de la listBox de pasos
        self.listBoxData = tk.Variable(value = self.data)

        #Generacion de la matriz
        self.genMatrix()
        self.hideMatrix()
        
        #Generacion del listBox
        self.listBoxMatrizCaminosPasos = tk.Listbox(self.Screen, height = 15, selectmode = tk.SINGLE, listvariable = self.listBoxData)
        
        #Vinculacion de evento al selecionar un paso
        self.listBoxMatrizCaminosPasos.bind('<<ListboxSelect>>', self.itemSelected)
                
    def reinicioVariables(self):
        self.matrix = np.array([])
        self.sizeMatrix = 0
        self.matrizCaminos = []
        self.data = []
                
    def setMatrix(self, matrix, size):
        #Define los datos obtenidos de Data Input
        #Matriz
        self.matrix = matrix
        #Tamaño matriz
        self.sizeMatrix = size

        #Copia la matrizOriginal a los pasos de matriz de caminos
        #self.copyMatrix(matrix)
        
        #Agrega a la lista la cantidad de pasos basado en el tamaño de matriz
        for index in range(int(self.sizeMatrix + 1)):
            self.listBoxMatrizCaminosPasos.insert(
                self.listBoxMatrizCaminosPasos.size(), "Paso " + str(index))

        #Configura el tamaño del listBox
        self.listBoxMatrizCaminosPasos.config(height = int(self.sizeMatrix+1))

        #Realiza la matriz de caminos a base de la matriz recibida
        self.walkMatrix()
        
    def showMatrix(self, paso):
        #Muestra la matriz
        #Posicion de la matriz
        posX = 240
        posY = 40

        #Mostrar matriz a base del paso actual y la posicion elegida
        for indexRow in range(int(self.sizeMatrix)):
            for indexColumn in range(int(self.sizeMatrix)):
                self.labelMatrix[indexRow][indexColumn].place(x=posX + indexColumn * 20, y=posY + indexRow * 20)
                self.dataMatrix[indexRow][indexColumn].set(self.matrizCaminos[paso][indexRow][indexColumn])

    def hideMatrix(self):
        #Modifica la matriz para que no sea visible por el usuario
        for indexRow in range(15):
            for indexColumn in range(15):
                self.labelMatrix[indexRow][indexColumn].place_forget()

    def genMatrix(self):
        #Genenra inicialmente la matriz
        #Posicion de la matriz
        posX = 240
        posY = 40

        #Genera la matriz para guardarla en las variables
        #DataMatrix --- Datos de la matriz
        #EntriesMatrix --- Datos de las entries de la matriz
        for indexRow in range(15):
            self.dataMatrix.append([])
            self.labelMatrix.append([])
            for indexColumn in range(15):
                self.dataMatrix[indexRow].append(tk.StringVar())
                self.labelMatrix[indexRow].append(
                    tk.Label(self.Screen, textvariable=self.dataMatrix[indexRow][indexColumn], width=2))
                self.labelMatrix[indexRow][indexColumn].place(x=posX + indexColumn * 20, y=posY + indexRow * 20)

    def show(self):
        #Muestra la matriz en el paso 0
        self.showMatrix(0)

        #Pasos listBox
        self.listBoxMatrizCaminosPasos.place(x = 30, y = 280)
    
    def hide(self):
        #Esconde la matriz
        self.hideMatrix()

        #Pasos listBox
        self.listBoxMatrizCaminosPasos.place_forget()
        
        self.reinicioVariables()

        
    def addDatafromRow(self, Row, tempRow):
        #Agrega datos a la fila basado en el linea selecionada
        if(len(Row) == len(tempRow)):
            for Column in range(1, len(Row)):
                if(tempRow[Column] == 1):
                    Row[Column] = tempRow[Column]

    def walkMatrix(self):
        #Realiza la matriz de caminos
        for Row in range(len(self.matrix)):
            self.copyMatrix(self.matrix)
            tmpRow = self.matrix[Row]
            for tempCol in range(len(self.matrix)):
                if tmpRow[tempCol] == 1:
                    self.addDatafromRow(self.matrix[Row], self.matrix[tempCol])
            for tempCol in range(len(self.matrix)):
                if tmpRow[tempCol] == 1:
                    self.addDatafromRow(self.matrix[Row], self.matrix[tempCol])

        print(self.matrix)

    def copyMatrix(self, matrix):
        #Copia la matriz a matriz de caminos para mostralo por pasos
        matrixTMP = np.array([[0 for x in range(self.sizeMatrix)]
                             for y in range(self.sizeMatrix)])
        
        for indexRow in range(self.sizeMatrix):
            for indexColumn in range(self.sizeMatrix):
                matrixTMP[indexRow][indexColumn] = matrix[indexRow][indexColumn]
        
        self.matrizCaminos.append(matrixTMP)

    def itemSelected(self, event):
        #Muestra la matriz a base del paso selecionado
        optionSelected = self.listBoxMatrizCaminosPasos.curselection()
        
        self.hideMatrix()
        self.showMatrix(optionSelected[0] - 1)