import pandas as pd
import xlrd
import os
p = os.path.dirname(os.getcwd()) #devuelve el path del directorio donde se encuentra actualmente el worksapce
os.chdir(p+ "/parcial 1")
def escribir():
    A = open('funcioneOS.txt','w')
    A.write("""Funcion de un sistema operativo
    1. Gestionar procesos o recursos para que los programas puedan ejecutarse de manera correcta.
    2.multiusuario capacidad de identificar diferentes usuarios y asignar privilegios
    3.Administrar la memoria principal del dispositivo, de modo que aunque varios programas se pongan en marcha, cada uno cuente con una entrada de memoria independiente
    4.Detectar errores, mantener la operatividad y controlar dispositivos, de manera que se eviten las interrupciones.
    5.multiprocesamiento asimetrico y simetrico""")
    A.close()

def crearEXC ():
    I = open("funcioneOS.txt", 'r')
    df= pd.DataFrame(data= I)
    s= df.to_excel("funciones.xlsx")
escribir()
crearEXC()
