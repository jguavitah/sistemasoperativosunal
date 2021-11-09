import socket
import asyncio
import os
from sys import path
async def select_file():
    Path= os.path.join(os.getcwd(),"punto4\\archivo")

    with os.scandir(Path) as files:
        files=[files.name for files in files if files.is_file() and files.name.endswith('.txt')]
    print("seleccione un archivo a subir")
    for i in files:
        num= files.index(i)+1
        print(num,i)
    
    return files[int(input())-1]

async def data_file(name):
    
    path= os.path.join(os.getcwd(),"punto4\\archivo\\{x}".format(x=name))
    
    with open(path,'r') as f:
        data_in_file=f.read()
    return data_in_file
    

async def send_file(data):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((socket.gethostname(),1234))
        file=s.send(str.encode(data)) 
        print("data send")

async def main():    
   # with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    #    s.connect((socket.gethostname(),1234))
        
     #   prueba=True
      #  data=s.send(bytes(prueba))
    file_name=await select_file()
    file_to_send=await data_file(file_name)
    task1= asyncio.create_task(send_file(file_to_send))
        

asyncio.run(main())


    