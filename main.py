import tkinter as tk
from tkinter import ttk

global mainWindow

#Inicio applicacion
mainWindow = tk.Tk()

#Configuracion
mainWindow.title('Proyecto - Matematica Computacional - ( 2023 - 2 ) - Grupo 5')
mainWindow.geometry("800x600")

sizeMatrix = tk.StringVar()
sizeMatrix.set("0")

def checkEntrySize():    
    print(sizeMatrix.get())
    sizeMatrixEntryData = sizeMatrix.get()
    sizeMatrixEntryData.replace(" ", "")

    if int(sizeMatrixEntry) == 0:
        print(True)

    if not str(sizeMatrixEntryData).isdigit():
        print(False)

    sizeMatrixEntryData = int(sizeMatrixEntryData)
    if not (sizeMatrixEntryData >= 5 and sizeMatrixEntryData <= 10):
        print(False)

    print(True)

#Tamaño matriz
tk.Label(mainWindow, text = "Size of Matrix: ").grid(row = 0)
sizeMatrixEntry = tk.Entry(mainWindow, textvariable = sizeMatrix).grid(row=0, column=1)

button = tk.Button(mainWindow, text="Submit", bg='bisque3',width=15, command=checkEntrySize).grid(row = 0, column = 2)

#Ejecucion applicacion
mainWindow.mainloop()