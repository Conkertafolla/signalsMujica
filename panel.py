#librerias tkinter
from tkinter import *
from tkinter import ttk


#librerias matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
from matplotlib.pyplot import show
import matplotlib.animation as animation
from matplotlib import style

#matplotlib use("TkAgg")

#libreria numpy
import numpy as np
from numpy import arange, sin, pi


#Variables de la señal
amplitud=1
frecuencia=1
fase=0
muestras=5 #numero de muestras a obtener
periodo=arange(0.0, 2*pi, 0.001)

#Datos para las tablas
datos_muestra=[]
rango_muestras=[]
identificador_tabla=[]

f=Figure()
ax=f.add_subplot(2,1,1)
ax1=f.add_subplot(2,1,2)




def datosSenal(amplitud,frecuencia,fase):
    return np.sin(((periodo)*frecuencia)+fase)*amplitud

def muestreo (amplitud,frecuencia,fase,muestras,n):
    return np.sin(((n)*frecuencia)+fase)*amplitud

def datosTabla(amplitud,frecuencia,fase,muestras,n):
    rango_muestras=n
    numero_renglones=len(n)
    datos_muestra=muestreo(amplitud,frecuencia,fase,muestras,n)
    for renglon in reversed(range(0,len(rango_muestras))):
        identificador_tabla.append(tree.insert("",0,text="{0:.2f}".format(rango_muestras[renglon]),values=("{0:.2f}".format(datos_muestra[renglon]))))

def limpiarTabla():
    if(len(identificador_tabla)>0):
        for i in range(0,len(identificador_tabla)):
            tree.delete(identificador_tabla[i])
    else:
        pass



def animacion(amplitud,frecuencia,fase,muestras):
    ax.clear()
    ax1.clear()
    limpiarTabla()
    ax.set_title("Señal original")
    ax.plot(periodo, datosSenal(amplitud,frecuencia,fase))
    n=np.linspace(0,2*pi,muestras)
    datos_muestra=muestreo(amplitud,frecuencia,fase,muestras,n)
    ax1.set_title('Señal muestreada')
    ax1.stem(n,datos_muestra)
    datosTabla(amplitud,frecuencia,fase,muestras,n)
    f.canvas.show()




def datosGrafica():
    amplitud=int(textAmplitud.get('1.0','end-1c'))
    frecuencia=int(textFrecuencia.get('1.0','end-1c'))
    fase=int(textFase.get('1.0','end-1c'))
    muestras=int(textmuestras.get('1.0','end-1c'))
    animacion(amplitud,frecuencia,fase,muestras)




#Define la ventana de la aplicacion
raiz=Tk()
#Definimos el tamaño
raiz.geometry('1200x800')
#Define el titulo
raiz.title('Programa de señales')


#Amplitud
labelAmplitud= Label(raiz, text="Amplitud")
labelAmplitud.place(x=30 ,y=20)
textAmplitud=Text(raiz,height=1,width=3)
textAmplitud.place(x=85 ,y=20)

#Frecuencia
labelFrecuencia= Label(raiz, text="Frecuencia")
labelFrecuencia.place(x=120,y=20)
textFrecuencia=Text(raiz,height=1,width=3)
textFrecuencia.place(x=180 ,y=20)

#Fase
labelFase= Label(raiz, text="Fase")
labelFase.place(x=220 ,y=20)
textFase=Text(raiz,height=1,width=3)
textFase.place(x=250 ,y=20)

#numero de muestras
labelmuestras= Label(raiz, text="Número de muestras")
labelmuestras.place(x=290, y=20)
textmuestras= Text (raiz, height=1, width=3)
textmuestras.place(x=410, y=20)

#Grafica boton
graficabtn= Button(raiz, height=1,width=10,text="Graficar", command=datosGrafica)
graficabtn.place(x=500, y=15)

#Creando tablas
tree=ttk.Treeview(raiz,columns=("muestras"))
tree.column("muestras", width=100)
tree.heading("#0",text=" n ")
tree.heading("muestras",text=" Valor de muestra")
tree.place(x=700, y=20)



canvas=FigureCanvasTkAgg(f,master=raiz)
canvas.get_tk_widget().place(x=30,y=60)
canvas.show()
ani=animation.FuncAnimation(f, animacion(amplitud,frecuencia,fase,muestras), interval=1000,)
f.tight_layout()


raiz.mainloop()
