import os
print("nombre del archivo a cambiar el nombre")
NAME = input()
print("nuevo nombre:")
NEW_NAME= input()
def Rename(a,b):
    os.rename(a,b) # os.rename cumple la funcion de cambiar el nombre de un archivo
Rename(NAME,NEW_NAME)