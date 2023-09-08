import tkinter as tk

global mainWindow

#Inicio applicacion
mainWindow = tk.Tk()

#Configuracion
mainWindow.title('Proyecto - Matematica Computacional - ( 2023 - 2 ) - Grupo 5')
mainWindow.geometry("800x600")

#Tamaño matriz
tk.Label(mainWindow, text = "Size of Matrix: ").grid(row = 0)
sizeMatrixEntry = tk.Entry(mainWindow).grid(row = 0, column = 1)



#Ejecucion applicacion
mainWindow.mainloop()