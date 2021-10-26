import os
print("Nombre de la carpeta a crear:")
FOLDER_NAME = input() 
def Make_folder(a) :
    os.mkdir(a) # os.mkdir permite crear un directorio nuevo 

Make_folder(FOLDER_NAME)
