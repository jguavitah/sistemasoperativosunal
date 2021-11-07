import socket
import asyncio
import os
from typing import Collection
p = os.path.dirname(os.getcwd()) 
os.chdir(p + "/parcial 1/punto3")



async def read_html(): #funcion para leer contenido de un htmml
    path = os.path.join(os.getcwd(),"prueba.html")
    with open(path, 'r') as file:
        msg = file.read()
    return msg

async def envio():
    
    PORT = 1234       
   
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: #creacion del socket servidor
        s.bind((socket.gethostname(), PORT))
        s.listen()
        
        client_socket, addr = s.accept() 
        with client_socket:
            data = await read_html() #await a el retorno del la anterior funcion
            client_socket.send(bytes(data,"utf-8")) #codifica en bytes la informacion


   


asyncio.run(envio())
        






