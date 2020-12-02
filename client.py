from socket import *
from ast import *

s = socket()
host = gethostname()
port = 12340

s.connect((host, port))

s.send(str(["test", "x"]).encode())
print(eval(s.recv(1024))[0])

s.close()
