import tkinter as tk
    
class dataInput():
    global mainWindow
    
    global sizeMatrixLabel
    global sizeMatrixEntry
    
    global statusMatrixLabel
    global infMatrixLabel
    
    def __init__(self, WindowFrame):
        mainWindow = WindowFrame.master
    
    def show(self, sizeMatrix, infMatrix):
        #Ingreso datos tamaño matriz
        sizeMatrixLabel = tk.Label(
            mainWindow, text="Tamaño de la matriz:").place(x=10, y=10)

        sizeMatrixEntry = tk.Entry(
            mainWindow, textvariable=sizeMatrix).place(x=10, y=40)

        #Informacion del dato ingresado
        statusMatrixLabel = tk.Label(mainWindow, text="Status").place(x=0, y=80)
        infMatrixLabel = tk.Label(mainWindow, text="Ingrese la informacion de la matriz",
                              textvariable=infMatrix).place(x=0, y=100)

        
    """
    def infDataInput():
        #Ingreso datos tamaño matriz
        sizeMatrixLabel = tk.Label(
            mainWindow, text="Tamaño de la matriz:").place(x=10, y=10)

        sizeMatrixEntry = tk.Entry(
            mainWindow, textvariable=sizeMatrix).place(x=10, y=40)

        #Informacion del dato ingresado
        statusDTLabel = tk.Label(mainWindow, text="Status").place(x=0, y=80)
        infDTLabel = tk.Label(mainWindow, text="Ingrese la informacion de la matriz",
                              textvariable=infMatrix).place(x=0, y=100)


    def hideMatrix(WindowFrame, matrixData, entriesMatrix):
        mainWindow = WindowFrame.master

        for indexRow in range(15):
            for indexColumn in range(15):
                entriesMatrix[indexRow][indexColumn].place_forget()

    def showMatrix(sizeMatrix, WindowFrame, matrixData, entriesMatrix):
        mainWindow = WindowFrame.master

        posX = 100
        posY = 100

        for indexRow in range(sizeMatrix):
            for indexColumn in range(sizeMatrix):
                entriesMatrix[indexRow][indexColumn].place(
                    mainWindow, x=posX + indexColumn * 20, y=posY + indexRow * 20)

    def genMatrix():
        posX = 100
        posY = 100

        for indexRow in range(15):
            matrixData.append([])
            entriesMatrix.append([])
            for indexColumn in range(15):
                matrixData[indexRow].append(tk.StringVar())
                entriesMatrix[indexRow].append(
                    tk.Entry(mainWindow, textvariable=matrixData[indexRow][indexColumn], width=2))
                entriesMatrix[indexRow][indexColumn].place(
                    x=posX + indexColumn * 20, y=posY + indexRow * 20)
     
#Ingreso de datos
#Aleatorio
#def dataRandom(sizeMatrix):


#Manual
#def dataManual(sizeMatrix):
"""