import hashlib
import os


path=os.path.join(os.getcwd(),"punto1.py")
with open(path,'rb') as f:
    data= f.read()
    
    hash1= hashlib.sha1()
    hash1.update(data)
    print('{}:{}'.format(hash1.name,hash1.hexdigest()))

path=os.path.join(os.getcwd(),"punto2\\punto2.py")
with open(path,'rb') as f:
    data= f.read()
   
    hash2= hashlib.sha1()
    hash2.update(data)
    print('{}:{}'.format(hash2.name,hash2.hexdigest()))

path=os.path.join(os.getcwd(),"punto3\\servidor.py")
with open(path,'rb') as f:
    data= f.read()
    
    hash3= hashlib.sha1()
    hash3.update(data)
    print('{}:{}'.format(hash3.name,hash3.hexdigest()))

path=os.path.join(os.getcwd(),"punto4\\cliente.py")
with open(path,'rb') as f:
    data= f.read()
   
    hash4= hashlib.sha1()
    hash4.update(data)
    print('{}:{}'.format(hash4.name,hash4.hexdigest()))


