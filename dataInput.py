import tkinter as tk



global parentFrame

def hederarFrame(WindowFrame):
    parentFrame = WindowFrame.master

def generateMatrix(WindowFrame, matrixData, entriesMatrix):
    mainWindow = WindowFrame.master
    
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

#Shows the matrix based on the option selected
def showMatrix(sizeMatrix, WindowFrame, matrixData, entriesMatrix):
    mainWindow = WindowFrame.master

    posX = 100
    posY = 100
    
    for indexRow in range(sizeMatrix):
        for indexColumn in range(sizeMatrix):
            entriesMatrix[indexRow][indexColumn].place(mainWindow, x=posX + indexColumn * 20, y=posY + indexRow * 20)

#Max size 15x15


def hideMatrix(WindowFrame, matrixData, entriesMatrix):
    mainWindow = WindowFrame.master
    
    for indexRow in range(15):
        for indexColumn in range(15):
            entriesMatrix[indexRow][indexColumn].place_forget()

#Ingreso de datos
#Aleatorio


#Manual
