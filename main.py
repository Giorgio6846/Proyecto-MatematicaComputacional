import tkinter as tk 

#Creacion del frame
global mainWindow

#Inicio applicacion
mainWindow = tk.Tk()

#Configuracion
mainWindow.title('Proyecto - Matematica Computacional - ( 2023 - 2 ) - Grupo 5 - Seccion SS41')
mainWindow.geometry("800x600")
mainWindow.resizable(False, False)

#Inicializacion de la variable sizeMatrix
sizeMatrix = tk.StringVar()
sizeMatrix.set("0")

#Informacion acerca del labelMatrix
infMatrix = tk.StringVar()
infMatrix.set("Ingrese la informacion de la matriz")

#Informacion matriz
global matrixData
global entriesMatrix

matrixData = []
entriesMatrix = []

def checkEntrySize():
    #Return
    # 0 Inicializacion
    # 1 Invalid Int
    # 2 True
        
    print(sizeMatrix.get())
    sizeMatrixData = sizeMatrix.get()
    sizeMatrixData = sizeMatrixData.replace(" ", "")

    print(type(sizeMatrixData))

    if not str(sizeMatrixData).isdigit():
        infMatrix.set("El valor de la matriz ingresada no es valida. Ingrese el valor entre 5 a 15")
        return 1

    if int(sizeMatrixData) == 0:
        infMatrix.set("El valor de la matriz ingresada no es valida. Ingrese el valor entre 5 a 15")
        return 0

    sizeMatrixData = int(sizeMatrixData)
    if not (sizeMatrixData >= 5 and sizeMatrixData <= 15):
        infMatrix.set("El valor de la matriz ingresada no es valida. Ingrese el valor entre 5 a 15")
        return 1

    infMatrix.set("El valor de la matriz exitoso")
    return 2



def checkMatrix():
    if checkEntrySize() == 2:
        #if len(matrixData) != 0:
        #    deleteMatrix()
        genMatrix(int(sizeMatrix.get()))

def genMatrix():
    posX = 100
    posY = 100
    
    for indexRow in range(15):
        matrixData.append([])
        entriesMatrix.append([])
        for indexColumn in range(15):
            matrixData[indexRow].append(tk.StringVar())
            entriesMatrix[indexRow].append(tk.Entry(mainWindow, textvariable= matrixData[indexRow][indexColumn], width = 2))
            entriesMatrix[indexRow][indexColumn].place(x = posX + indexColumn * 20, y = posY + indexRow * 20)

def showMatrix(sizeMatrix):
    posX = 100
    posY = 100
    
    for indexRow in range(sizeMatrix):
        for indexColumn in range(sizeMatrix):
            entriesMatrix[indexRow][indexColumn].place(x = posX + indexColumn * 20, y = posY + indexRow * 20)
    
#Max size 15x15
def hideMatrix():
    for indexRow in range(15):
        for indexColumn in range(15):
            entriesMatrix[indexRow][indexColumn].place_forget()        
                    
#Tamaño matriz
tk.Label(mainWindow, text = "Size of Matrix: ").place(x = 0, y = 0)
sizeMatrixEntry = tk.Entry(mainWindow, textvariable = sizeMatrix).place(x = 90, y = 0)
button = tk.Button(mainWindow, text="Generate Matrix",
                   width=15, command=checkMatrix).place(x=220, y=0)

button1 = tk.Button(mainWindow, text="Generate Matrix",
                    width=15, command=genMatrix).place(x=220, y=40)

button1 = tk.Button(mainWindow, text="Generate Matrix",
                   width=15, command=hideMatrix).place(x=220, y=60)


tk.Label(mainWindow, text = "Ingrese la informacion de la matriz", textvariable = infMatrix).place(x = 0, y = 25)



#Configurar los tamaños de la pantalla
#mainWindow.rowconfigure(0, weight = 1)

#Ejecucion applicacion
mainWindow.mainloop()