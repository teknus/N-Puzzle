from Npuzzle import Board, BoardH
from os import path

m = BoardH()

pth = path.abspath("")
pth = pth[:len(pth)-3]+"test3.txt"
m.loadMatrix(pth)
obj = BoardH()
obj.loadMatrix(pth)
print("Pre shuffle")
print(m)
m.shuffleInstance(500)
print(m)
print("A*")
exp, b = m.aStar(obj,m)
print(len(exp),b)
print("IDA*")
exp, b = m.idaStar(obj,m)
print(len(exp),b)