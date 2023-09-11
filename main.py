import tkinter as tk 

#Archivos adicionales
import dataInput as dt
import dataInputv2 as dt

#Creacion del frame 
global mainWindow
mainWindow = tk.Tk()

#Variables Interfaz
#MatrixData
global matrixData
matrixData = []

#EntriesMatrix
global entriesMatrix
entriesMatrix = []

#Configuracion del app
mainWindow.title('Proyecto - Matematica Computacional - ( 2023 - 2 ) - Grupo 5 - Seccion SS41')
mainWindow.geometry("800x600")
mainWindow.resizable(False, False)
mainWindow.config(background = 'grey')

#Variables
#sizeMatrix
sizeMatrix = tk.StringVar()
sizeMatrix.set("0")
#labelMatrix
infMatrix = tk.StringVar()
infMatrix.set("Ingrese la informacion de la matriz")
#OpcionIngreso
typeEntry = tk.StringVar()

def verificacionSizeMatrix():
    # Output Data
    # 0 El entry tiene 0
    # 1 El entry tiene un dato no valido 
    # 2 El entry tiene un dato valido

    sizeMatrixData = sizeMatrix.get()
    sizeMatrixData = sizeMatrixData.replace(" ", "")

    if not str(sizeMatrixData).isdigit():
        infMatrix.set("El valor de la matriz ingresada no es valida. Ingrese el valor entre 5 a 15")
        return 1
    
    sizeMatrixData = int(sizeMatrixData)
    if sizeMatrixData == 0:
        infMatrix.set("El valor de la matriz ingresada no es valida. Ingrese el valor entre 5 a 15")
        return 0

    if not (sizeMatrixData >= 5 and sizeMatrixData <= 15):
        infMatrix.set("El valor de la matriz ingresada no es valida. Ingrese el valor entre 5 a 15")
        return 1

    infMatrix.set("El valor de la matriz exitoso")
    return 2

#GenMatrix
def matrixDataControlller():
    if len(matrixData) == 0:
        dt.generateMatrix(mainWindow,
                      matrixData, entriesMatrix)
    
    if verificacionSizeMatrix() == 2:
        dt.hideMatrix(mainWindow,
                      matrixData, entriesMatrix)
        dt.showMatrix(int(sizeMatrix.get()), mainWindow,
                      matrixData, entriesMatrix)

#Ingreso datos tamaño matriz
#tk.Label(mainWindow, text = "Tamaño de la matriz:").place(x = 10, y = 10)
#sizeMatrixEntry = tk.Entry(mainWindow, textvariable = sizeMatrix).place(x = 10, y = 40)

#Informacion del dato ingresado
#tk.Label(mainWindow, text = "Status").place(x = 0, y = 80)

#tk.Label(mainWindow, text = "Ingrese la informacion de la matriz", textvariable = infMatrix).place(x = 0, y = 100)
                    
#button = tk.Button(mainWindow, text="Generate Matrix", width=15,
#                   command=matrixDataControlller).place(x=260, y= 0)

#Frames
#Menu
menuFrame = tk.Frame(mainWindow, width = 200, height = 200, bg = 'white')
menuFrame.place(x = 20, y = 20)

#SubMenu
subMenuFrame = tk.Frame(mainWindow, width = 200, height = 340, bg = 'white')
subMenuFrame.place(x = 20, y = 240)

#Vista
viewFrame = tk.Frame(mainWindow, width = 540, height = 560, bg = 'white')
viewFrame.place(x = 240, y = 20)

#Opciones de usuario
buttonData = tk.Button(mainWindow, text="Ingreso datos", width=15,
                   command=matrixDataControlller).place(x=30, y=20)
buttonMatrix = tk.Button(mainWindow, text="Matriz de Caminos ", width=15,
                   command=matrixDataControlller).place(x=30, y=40)
buttonComponentesConexas = tk.Button(mainWindow, text="Componentes Conexas", width=15,
                   command=matrixDataControlller).place(x=30, y=70)

#Ejecucion applicacion
mainWindow.mainloop()