from tkinter import *
from tkinter import ttk
from numpy import arange, sin, pi
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

COUNT = 100 #Numero de iteraciones
fig=plt.figure()  #declaramos el frame y el handler de la grafica
               #arreglo para almacenar los datos de Y

#Variables para los datos de la señal original
t=arange(0.0,2*pi,0.01)
amplitud=0
frecuencia=0
fase=0

def grafica (amplitud,frecuencia,fase): 
    ax1 = fig.add_subplot(111)
    ax1.plot(t,np.sin(((t)*frecuencia)+fase)*amplitud)
    ax1.set_ylim((-amplitud, amplitud))
    ax1.set_xlim(0, 2*pi) 
    ax1.set_ylabel('1 Hz')
    ax1.set_title('A sine wave or two')
    for label in ax1.get_xticklabels():
        label.set_color('r')
    plt.show()


def datosGrafica():
    global amplitud
    global frecuencia
    global fase
    amplitud=int(textAmplitud.get('1.0','end-1c'))
    frecuencia=int(textFrecuencia.get('1.0','end-1c'))
    fase=int(textFase.get('1.0','end-1c'))
    grafica(amplitud,frecuencia,fase)
    
 


#Define la ventana de la aplicacion
raiz=Tk()
#Definimos el tamaño
raiz.geometry('1000x600')
#Define el titulo
raiz.title('Programa de señales')


#Amplitud
labelAmplitud= Label(raiz, text="Amplitud")
labelAmplitud.place(x=30 ,y=20)
textAmplitud=Text(raiz,height=1,width=5)
textAmplitud.place(x=85 ,y=20)

#Frecuencia
labelFrecuencia= Label(raiz, text="Frecuencia")
labelFrecuencia.place(x=120,y=20)
textFrecuencia=Text(raiz,height=1,width=5)
textFrecuencia.place(x=180 ,y=20)

#Fase
labelFase= Label(raiz, text="Fase")
labelFase.place(x=220 ,y=20)
textFase=Text(raiz,height=1,width=5)
textFase.place(x=250 ,y=20)

#Grafica boton
graficabtn= Button(raiz, height=1,width=10,text="Graficar", command=datosGrafica)
graficabtn.place(x=300, y=15)

#Limpiar boton
"""limpiarbtn= Button(raiz, height=1,width=10,text="Limpiar", command=limpiarGrafica)
limpiarbtn.place(x=380, y=15)"""

#numero de muestras
labelmuestras= Label(raiz, text="Número de muestras")
labelmuestras.place(x=720, y=20)
textmuestras= Text (raiz, height=1, width=10)
textmuestras.place(x=850, y=20)

#numero de armonicos de la serie
labelarmonicos= Label(raiz,text="Número de armonicos")
labelarmonicos.place(x=720,y=40)
textarmonicos=Text(raiz,height=1,width=10)
textarmonicos.place(x=850, y=40)

#Frame para la grafica dentro de la pantalla




raiz.mainloop()