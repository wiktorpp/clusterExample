from socket import *
from ast import *

s = socket()
host = gethostname()
port = 12340
s.bind((host, port))

def test(str): return str

s.listen(5)
while True:
    c, addr = s.accept()
    array = literal_eval(c.recv(4096).decode())
    c.send(str(globals()[array[0]](array[1:])).encode())
    c.close()
