#librerias matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from matplotlib.pyplot import show

#librerias numpy
import numpy as np
from numpy import arange, sin, pi

amplitud=1
frecuencia=1
periodo=arange(0.0, 2*pi, 0.01)

#Funcion para generar los datos a Graficar
def datosSenal(amplitud,frecuencia,fase):
    return np.sin(((periodo)*frecuencia)+fase)*amplitud

#funcion para graficar
def grafica (amplitud,frecuencia,fase):
    f=Figure()
    ax1=f.add_subplot(211)
    ax1.plot(periodo, datosSenal(amplitud,frecuencia,fase))
    ax2=f.add_subplot(212)
    ax2.plot(periodo, datosSenal(amplitud-2,frecuencia,fase))
    show()




amplitud=int(input("\nIntroducir la amplitud de la señal: "))
frecuencia=int(input("\nFrecuencia de la señal"))
fase=int(input("\nFase de la señal"))
grafica(amplitud,frecuencia,fase)
