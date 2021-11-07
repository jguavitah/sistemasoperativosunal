import socket
import webbrowser
import os
p = os.path.dirname(os.getcwd()) #devuelve el path del directorio donde se encuentra actualmente el worksapce
os.chdir(p + "/parcial 1/punto3")
  
PORT = 1234      

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((socket.gethostname(), PORT))
    data = s.recv(1024)

ruta = os.path.join(os.getcwd(),"nuevo.html")

with open(ruta, 'w') as file:      
    file.write(data.decode("utf-8"))

webbrowser.open_new_tab(ruta)