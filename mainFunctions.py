import tkinter as tk


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
