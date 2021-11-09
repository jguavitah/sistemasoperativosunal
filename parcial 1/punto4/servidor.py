import socket
import asyncio
import os;
from typing import Collection
p = os.path.dirname(os.getcwd()) 
os.chdir(p + "/parcial 1")





async def envio_lista(file):
    path= path= os.path.join(os.getcwd(),"punto4\\archivo_servidor")
    print("info recibida en :", path)
    print(file)
    return False
    



          
   
    
      
async def Get_info():
    s = socket.socket (socket.AF_INET,socket.SOCK_STREAM)
    s.bind((socket.gethostname(),1234))
    s.listen(5)
    clientsocket,address= s.accept()
    files=clientsocket.recv(1024)
    print("info recibida")
    path= os.path.join(os.getcwd(),"punto4/archivo_servidor/archivo1.txt")
    data=files.decode()
    with open(path,"w")as f:
        f.write(data)
    

    return data

        


async def main():
    final=True
    while final ==True:
        print("iniciando ciclo")      
        task1= asyncio.create_task(Get_info())
        data= await task1
        task2= asyncio.create_task(envio_lista(data))
        final= await task2
        

        
       

   


asyncio.run(main())




