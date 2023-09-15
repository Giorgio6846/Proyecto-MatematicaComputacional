import tkinter as tk
import numpy as np

class componentesConexas:
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

        self.listComponentesConexas = []

        self.genMatrix()
        self.hideMatrix()
    
    def reinicioVariables(self):


        #Variables
        #Data Matrix
        for indexRow in range(self.sizeMatrix):
            for indexColumn in range(self.sizeMatrix):
                self.dataMatrix[indexRow][indexColumn].set(0)
        #Datos Matriz
        self.matrix = np.array([])
        #Tamaño Matriz
        self.sizeMatrix = 0        

        self.listComponentesConexas = []
        
    def show(self):
        self.showMatrix()

    def hide(self):
        self.hideMatrix()

    def setMatrix(self, matrix, size):
        self.reinicioVariables()

        #Define los datos obtenidos de Data Input
        #Matriz
        matrixTMP = matrix
        #Tamaño matriz
        self.sizeMatrix = size

        self.matrix = np.array([[matrixTMP[y][x] for x in range(self.sizeMatrix)] for y in range(self.sizeMatrix)])
        print(self.matrix)

        row = np.array([(x) for x in range(self.sizeMatrix + 1)])
        col = np.array([(y + 1) for y in range(self.sizeMatrix)])

        self.matrix = np.insert(self.matrix, 0, col, axis = 1)
        self.matrix = np.insert(self.matrix, 0, row, axis = 0)
        print(self.matrix)
        
        self.sortMaxtoMin()
        self.sortColumn()
        
        self.detectComponentesConexas()
        
    def showMatrix(self):
        #Muestra la matriz
        #Posicion de la matriz
        posX = 240
        posY = 40

        #Mostrar matriz a base del paso actual y la posicion elegida
        for indexRow in range(int(self.sizeMatrix) + 1):
            for indexColumn in range(int(self.sizeMatrix) + 1):
                if indexRow == 0 or indexColumn == 0:
                    self.labelMatrix[indexRow][indexColumn].config(
                        fg="#ff0000")

                self.labelMatrix[indexRow][indexColumn].place(
                    x=posX + indexColumn * 20, y=posY + indexRow * 20)
                self.dataMatrix[indexRow][indexColumn].set(
                    self.matrix[indexRow][indexColumn])

    def hideMatrix(self):
        #Modifica la matriz para que no sea visible por el usuario
        for indexRow in range(15 + 1):
            for indexColumn in range(15 + 1):
                self.labelMatrix[indexRow][indexColumn].place_forget()

    def genMatrix(self):
        #Genenra inicialmente la matriz
        #Posicion de la matriz
        posX = 240
        posY = 40

        #Genera la matriz para guardarla en las variables
        #DataMatrix --- Datos de la matriz
        #EntriesMatrix --- Datos de las entries de la matriz
        for indexRow in range(15 + 1):
            self.dataMatrix.append([])
            self.labelMatrix.append([])
            for indexColumn in range(15 + 1):
                self.dataMatrix[indexRow].append(tk.StringVar())
                self.labelMatrix[indexRow].append(
                    tk.Label(self.Screen, textvariable=self.dataMatrix[indexRow][indexColumn], width=2))
                self.labelMatrix[indexRow][indexColumn].place(
                    x=posX + indexColumn * 20, y=posY + indexRow * 20)

    #Ordenamiento de filas de mayor a menor
    def sortMaxtoMin(self):
        for Row in range(1, len(self.matrix)):
            maxValue = [0, 0]
            for tmpRow in range(Row, len(self.matrix)):
                if self.count1Row(self.matrix[tmpRow]) > maxValue[0]:
                    maxValue = [self.count1Row(self.matrix[tmpRow]), tmpRow]
            self.swapRows(Row, maxValue[1])

    def count1Row(self, Row):
        amountof1 = 0
        for Column in range(1,len(Row)):
            if Row[Column] == 1:
                amountof1 = amountof1 + 1
        return amountof1
    
    def swapRows(self, row1, row2):
        rowTMP = np.copy(self.matrix[row2])
        self.matrix[row2] = self.matrix[row1]
        self.matrix[row1] = rowTMP
        
    def sortColumn(self):
        for Row in range(1, len(self.matrix)):
            for tmpRow in range(Row, len(self.matrix)):
                if self.matrix[Row][0] == self.matrix[0][tmpRow] and Row != tmpRow:
                    self.swapColumns(Row, tmpRow)
        
    def swapColumns(self, col1, col2):
        for row in range(len(self.matrix)):
            cellTMP = self.matrix[row][col1]
            self.matrix[row][col1] = self.matrix[row][col2]
            self.matrix[row][col2] = cellTMP

    def detectComponentesConexas(self):
            startValue = 0
            listTMP = []
            
            for index in range(1,len(self.matrix)):
                if startValue == 0:
                    startValue = index
                    listTMP.append(self.matrix[index][0])
                else:
                    if self.verifySquare1(startValue,index):
                        print(index, "1a", self.matrix[index][0])


                        listTMP.append(self.matrix[index][0])

                        pass
                    elif startValue == index - 1:
                        print(index, "2a",self.matrix[index][0])
                        print(listTMP)

                        self.listComponentesConexas.append(listTMP)
                        listTMP = []                    
                        
                        listTMP.append(self.matrix[index][0])

                        startValue = index
                    else:
                        print(index, "3a", self.matrix[index][0])
                        print(listTMP)
                        
                        self.listComponentesConexas.append(listTMP)
                        listTMP = []

                        listTMP.append(self.matrix[index][0])
                        startValue = index


            if int((self.listComponentesConexas[len(self.listComponentesConexas) - 1]
                                        [len(self.listComponentesConexas[len(self.listComponentesConexas) - 1]) - 1])) != int(self.matrix[len(self.matrix) - 1][0]):
                listTMP = []
                listTMP.append(self.matrix[len(self.matrix) - 1][0])

                print(listTMP)
                self.listComponentesConexas.append(listTMP)
                listTMP = []                

    def verifySquare1(self,indexStart, indexEnd):
        squareValid = True
        for indexRow in range(indexStart, indexEnd + 1):
            for indexColumn in range(indexStart, indexEnd + 1):
                if self.matrix[indexRow][indexColumn] == 0:
                    squareValid = False
                    break

        return squareValid