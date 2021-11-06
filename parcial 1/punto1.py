import pandas as pd
import xlrd
import os
p = os.path.dirname(os.getcwd()) #devuelve el path del directorio donde se encuentra actualmente el worksapce
os.chdir(p+ "/parcial 1")
def escribir():
    A = open('funcioneOS.txt','a')
    A.write("""Funcion de un sistema operativo
    1. multitareas
    2.multiusuario capacidad de identificar diferentes usuarios y asignar privilegios
    3.multiprocesamiento o multiprocesador
    4capacidad de dadministrar maquinas con varios cpus
    5.multiprocesamiento asimetrico y simetrico""")
    A.close()

def crearEXC ():
    I = open("funcioneOS.txt", 'r')
    df= pd.DataFrame(data= I)
    s= df.to_excel("funciones.xlsx")
escribir()
crearEXC()
