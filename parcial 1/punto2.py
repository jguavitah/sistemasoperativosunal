from asyncio import tasks
import socket
import ssl
import asyncio
import os
p = os.path.dirname(os.getcwd()) 
os.chdir(p + "/parcial 1/punto2")

async def llamada(lista,H,P): #creacion de sockets y request de informacion
    context= ssl.create_default_context()
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    Wrapped=context.wrap_socket(s,server_hostname=H)
    Wrapped.connect((H, P))
                 
    request = "{a} HTTP/1.0\r\nHost: www.buda.com\r\n\r\n".format(a= lista) 
        
    Wrapped.sendall(str.encode(request))
     
    while True:
        reply = Wrapped.recv(1024)
        if len(reply)<1:
            break
        print(lista)
        nombre= lista[28:]
        path = os.path.join(os.getcwd(),"{n}.txt".format(n = nombre))
        with open(path, 'w') as f:
            f.write(reply.decode())
    
            
    
        
async def main():
    HOST, PORT = "www.buda.com", 443 #host y port para realizar la coneccion del socket
    tipo_dato=['GET /api/v2/markets/eth-btc/order_book','GET /api/v2/markets/eth-btc/ticker','GET /api/v2/markets/eth-btc/trades']
    # una lista que guarda las request que se solicitan a buda.com
    for i in tipo_dato: 
        tasks = asyncio.create_task(llamada(i,HOST,PORT))
        await tasks
    print("enviado")    
    
      
       



asyncio.run(main())




# CLOSE SOCKET CONNECTION



