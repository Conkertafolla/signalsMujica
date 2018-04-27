#librerias matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from matplotlib.pyplot import show

#librerias numpy
import numpy as np
from numpy import arange, sin, pi,floor

amplitud=1
frecuencia=1
fase=0
muestras=0
periodo=arange(0.0, 2*pi, 0.001)

#Funcion para generar los datos a Graficar de la funcion original
def datosSenal(amplitud,frecuencia,fase):
    return np.sin(((periodo)*frecuencia)+fase)*amplitud

#funion para generar los datos a graficar de la funcion muestreada
def muestreo(amplitud,frecuencia,fase,muestras):
    t=1/muestras
    n=arange(0,2*pi)

    return arange(n*t,np.sin(((periodo)*frecuencia*t)+fase)*amplitud)



#funcion para graficar
def grafica (amplitud,frecuencia,fase,muestras):
    f=Figure()
    ax=f.add_subplot(211)
    plt.plot(periodo, datosSenal(amplitud,frecuencia,fase))
    ax=f.add_subplot(212)
    plt.plot(periodo, muestreo(amplitud,frecuencia,fase,muestras))
    show()




amplitud=int(input("\nIntroducir la amplitud de la señal: "))
frecuencia=int(input("\nFrecuencia de la señal"))
fase=int(input("\nFase de la señal"))
muestras=int(input("\nFrecuencia de muestreo"))
grafica(amplitud,frecuencia,fase,muestras)
