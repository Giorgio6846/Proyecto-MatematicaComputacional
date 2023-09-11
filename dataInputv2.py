import tkinter as tk



def showDataInput(WindowFrame):
    print()

def hideDataInput(WindowsFrame):
    print()
    
    
class dataInput:
    def __init__(self, m,m,.,,>?mnn,?>?>>n<?>nnm,,                    ; ;;  .WindowFrame):
        mainWindow = WindowFrame.master
    
    def show():
        #Ingreso datos tamaño matriz
        sizeMatrixLabel = tk.Label(
            mainWindow, text="Tamaño de la matriz:").place(x=10, y=10)
        sizeMatrixEntry = tk.Entry(
            mainWindow, textvariable=sizeMatrix).place(x=10, y=40)

        #Informacion del dato ingresado
        tk.Label(mainWindow, text = "Status").place(x = 0, y = 80)
        tk.Label(mainWindow, text = "Ingrese la informacion de la matriz", textvariable = infMatrix).place(x = 0, y = 100)
        
    def hide():
        print()