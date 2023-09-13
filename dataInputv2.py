import tkinter as tk
import numpy as np
import random

class dataInput:

    def __init__(self, Screen):
        #Frame tkinter
        self.Screen = Screen
       
        #Variables
        #Tamaño matriz
        self.sizeMatrix = tk.StringVar()
        self.sizeMatrix.set("0")
        #Status Matriz
        self.informacionMatriz = tk.StringVar()
        self.informacionMatriz.set("Ingrese la informacion de la matriz")
        #Matriz Data
        self.dataMatrix = []
        #Entries Data
        self.entriesMatrix = []
        #Opcion de entrada selecionada
        self.optionSelected = tk.IntVar()   
        #Matriz
        self.arrayFinal = np.array([[0 for x in range(15)] for y in range(15)])
        self.checkMatrix = False
        #DataInput
        self.checkDataInput = False

        #Generacion de la matriz
        self.genMatrix()
        self.hideMatrix()
        
        #Tamaño matriz
        #Label
        self.sizeMatrixLabel = tk.Label(self.Screen, text="Tamaño de la matriz:")
        #Entry
        self.sizeMatrixEntry = tk.Entry(self.Screen, textvariable=(self.sizeMatrix))
        
        #Status matriz
        #Label
        self.statusMatrix = tk.Label(self.Screen, text = "Status: ")
        self.statusModMatrix = tk.Label(self.Screen, text = "Ingrese la informacion de la matriz", textvariable = self.informacionMatriz)

        #Generar matriz
        #Button
        self.buttonGenerarMatriz = tk.Button(self.Screen, text = "Generar Matriz", width = 15, command = self.generarMatrizTamaño)

        #Opcion de entrada selecionada
        #RadioButton
        self.entradaSelecionadaAleatorio = tk.Radiobutton(self.Screen, text = "Aleatorio", variable = self.optionSelected, command = self.dataMatrizRandom, value = 1)
        self.entradaSelecionadaManual = tk.Radiobutton(self.Screen, text="Manual", variable=self.optionSelected, command = self.dataMatrizManual, value=2)

        #Guardar matriz
        #Button
        self.buttonGuardarMatriz = tk.Button(self.Screen, text="Guardar Matriz", width=15, command=self.guardarMatriz)

        #Reiniciar
        #Button
        self.buttonReiniciarMatriz = tk.Button(self.Screen, text="Reiniciar", width=15, command=self.reincioVariables)


    def reincioVariables(self):
        self.sizeMatrix.set("0")
        self.informacionMatriz.set("Ingrese la informacion de la matriz")

        self.sizeMatrixEntry.config(state = "normal")


        for indexRow in range(15):
            for indexColumn in range(15):
                self.entriesMatrix[indexRow][indexColumn].config(state = "normal")
                self.dataMatrix[indexRow][indexColumn].set(0)
                
        self.arrayFinal = []
        self.arrayFinal = np.array([[0 for x in range(15)] for y in range(15)])
        
        self.checkMatrix = False
        self.checkDataInput = False
        
        #Reinicio de Opcion
        self.optionSelected.set(None)
        
        self.checkMatrix = False


    def showMatrix(self):
        #Muestra la matriz
        #Posicion de la matriz
        posX = 240
        posY = 40

        #Mostrar matriz a base de la posicion
        for indexRow in range(int(self.sizeMatrix.get())):
            for indexColumn in range(int(self.sizeMatrix.get())):
                self.entriesMatrix[indexRow][indexColumn].place(x=posX + indexColumn * 20, y=posY + indexRow * 20)
                self.dataMatrix[indexRow][indexColumn].set(0)

        #Opcion de entrada
        self.entradaSelecionadaAleatorio.place(x = 20, y = 380)
        self.entradaSelecionadaManual.place(x = 20, y = 400)

        #Opcion de guardado
        self.buttonGuardarMatriz.place(x=20, y=420)

    def hideMatrix(self):
        #Modifica la matriz para que no sea visible por el usuario
        for indexRow in range(15):
            for indexColumn in range(15):
                self.entriesMatrix[indexRow][indexColumn].place_forget()

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
            self.entriesMatrix.append([])
            for indexColumn in range(15):
                self.dataMatrix[indexRow].append(tk.StringVar())
                self.entriesMatrix[indexRow].append(
                    tk.Entry(self.Screen, textvariable=self.dataMatrix[indexRow][indexColumn], width=2))
                self.entriesMatrix[indexRow][indexColumn].place(
                    x=posX + indexColumn * 20, y=posY + indexRow * 20)

    
    def show(self):
        #Status matrix
        #Label
        self.statusMatrix.place(x = 20, y = 240)
        self.statusModMatrix.place(x = 20, y = 260)

        #Tamaño matrix
        #Label
        self.sizeMatrixLabel.place(x=20, y=300)
        #Entry
        self.sizeMatrixEntry.place(x=20, y=320)

        #Generar Matriz
        #Button
        self.buttonGenerarMatriz.place(x = 20, y = 340)

        self.buttonReiniciarMatriz.place(x = 20, y = 500)

        #Reinicia las variables al seleccionar el boton de ingreso de datos        
        self.reincioVariables()
        
        
    def hide(self):
        #Tamaño matrix
        #Label
        self.sizeMatrixLabel.place_forget()
        #Entry
        self.sizeMatrixEntry.place_forget()
        
        #Status matrix
        #Label
        self.statusMatrix.place_forget()
        self.statusModMatrix.place_forget()
    
        #Generar Matriz
        #Button
        self.buttonGenerarMatriz.place_forget()
        self.hideMatrix()
    
        #Reinicio de Opcion
        self.optionSelected.set(None)
    
        self.entradaSelecionadaAleatorio.place_forget()
        self.entradaSelecionadaManual.place_forget()
        self.buttonGuardarMatriz.place_forget()
        
        self.buttonReiniciarMatriz.place_forget()
        
        #Reinicia las variables al seleccionar el boton de ingreso de datos        
        self.reincioVariables()
    
    def generarMatrizTamaño(self):
        #Genera el matriz con el tamaño deseado
        if self.verificacionSizeMatrix() == 2:
            #Esconde y muestra la matriz si habia una existente anteriormente
            self.hideMatrix()
            self.showMatrix()
        #Cambia esta variable para que no se pueda guardar antes de realizar la verificacion
        self.checkDataInput = False
        
        #Reinicio de Opcion
        self.optionSelected.set(None)

    
    def verificacionSizeMatrix(self):
        # Output Data
        # 0 El entry tiene 0
        # 1 El entry tiene un dato no valido
        # 2 El entry tiene un dato valido

        sizeMatrixData = self.sizeMatrix.get()
        sizeMatrixData = sizeMatrixData.replace(" ", "")

        if not str(sizeMatrixData).isdigit():
            self.informacionMatriz.set(
                "El valor de la matriz ingresada no es valida. Ingrese el valor entre 5 a 15")
            return 1

        sizeMatrixData = int(sizeMatrixData)
        if sizeMatrixData == 0:
            self.informacionMatriz.set(
                "El valor de la matriz ingresada no es valida. Ingrese el valor entre 5 a 15")
            return 0

        if not (sizeMatrixData >= 5 and sizeMatrixData <= 15):
            self.informacionMatriz.set(
                "El valor de la matriz ingresada no es valida. Ingrese el valor entre 5 a 15")
            return 1

        self.informacionMatriz.set("El valor de la matriz exitoso")
        return 2

    #Ingreso de datos
    #Aleatorio
    def dataMatrizRandom(self):
        #Los datos de la matriz creados aleatoriamente
        for indexRow in range(int(self.sizeMatrix.get())):
            for indexColumn in range(int(self.sizeMatrix.get())):
                self.dataMatrix[indexRow][indexColumn].set(self.percentage1Value())

    def percentage1Value(self):
        #Genera aleatoriamente el numero 1 con una probabilidad del 19%
        number = random.randint(1, 101)
        if number <= 19:
            number = 1
        else:
            number = 0
        return number

    #Manual
    def dataMatrizManual(self):
        #Los datos de la matriz son ingresados por el usuario
        
        #Modifica el entry de la matriz para que se pueda redactar en el
        for indexRow in range(15):
            for indexColumn in range(15):
                self.entriesMatrix[indexRow][indexColumn].config(state="normal")
    
    def checkMatriz(self):
        #Verifica si los datos ingresados en la matriz es 1 o 0
        for indexRow in range(int(self.sizeMatrix.get())):
            for indexColumn in range(int(self.sizeMatrix.get())):
                if not (self.dataMatrix[indexRow][indexColumn].get() == "1" or self.dataMatrix[indexRow][indexColumn].get() == "0"):
                    print(self.dataMatrix[indexRow][indexColumn].get())
                    self.informacionMatriz.set("Los datos ingresados en la matriz son incorrectos")
                    return False
        self.informacionMatriz.set("Los datos ingresados en la matriz estan correctos")
        return True
    
    #Guardar Matriz
    def guardarMatriz(self):
        #Guarda la matriz para que pueda ser utiliza en la clase MatrizCaminos
        if self.checkMatriz() == 1:
            #Al selecionar este boton guarda los datos asi como realizar que la matriz no pueda ser modificada           
            self.sizeMatrixEntry.config(state = "readonly")
            
            for indexRow in range(15):
                for indexColumn in range(15):
                    self.entriesMatrix[indexRow][indexColumn].config(state = "readonly")

            #Guarda la matriz en un array arrayFinal            
            for indexRow in range(int(self.sizeMatrix.get())):
                for indexColumn in range(int(self.sizeMatrix.get())):
                    self.arrayFinal[indexRow][indexColumn] = self.dataMatrix[indexRow][indexColumn].get()
            
        #Modifica la variable para que la clase controladora entienda que esta matriz si es valida
        self.checkDataInput = True

        #Modo debug
        print(self.arrayFinal)
    
    def getMatriz(self):
        #Retorna la matriz para que la clase tenga acceso
        self.arrayTMP = np.array([[0 for x in range(int(self.sizeMatrix.get()))]
                                 for y in range(int(self.sizeMatrix.get()))])

        for indexRow in range(int(self.sizeMatrix.get())):
            for indexColumn in range(int(self.sizeMatrix.get())):
                self.arrayTMP[indexRow][indexColumn] = self.arrayFinal[indexRow][indexColumn]
        
        return self.arrayTMP
    
    def getSizeMatrix(self):
        #Retorna el tamaño de la matriz
        return int(self.sizeMatrix.get())
    
    def getVerificacion(self):
        #Retorna la verificacion de la matriz
        print("VERIFICACION DE LA MATRIZ -- DATA INPUT --", end = " ")
        print(self.checkDataInput)
        return self.checkDataInput