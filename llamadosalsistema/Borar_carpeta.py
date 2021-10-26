import os
 
os.mkdir("carpeta de prueba") # se crea una carpeta de referencia
for NUM in range(1) :
    print(os.listdir()) # funcion de modulo os que permite ver los archivos de contiene un directorio
    os.rmdir('carpeta de prueba') # funcion del modulo os que permite borrar un directorio
    NUM += 1
print(os.listdir()) # volvemos a vizualizar los archivos para evidenciar que la carpeta de pruebas ha sido borrada