
def leer():
    f = open('file.txt',"r")
    mensaje = f.read()
    print(mensaje)
    f.close()

def escribir():
    leer()
    A = open('file.txt','a')
    text = input()
    A.write(text)
    A.close()

escribir()
leer()