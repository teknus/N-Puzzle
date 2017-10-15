from Npuzzle import Board
from os import path

m = Board()

pth = path.abspath("")
pth = pth[:len(pth)-3]+"matrix.txt"
m.loadMatrix(pth)
obj = Board()
obj.loadMatrix(pth)
print("Pre shuffle")
print(m)
m.moveDown()
m.moveRight()
m.moveRight()
m.moveUp()
m.moveUp()
print(m)
print("BFS")
exp, b = m.bfs(obj,m)
print(len(exp),b)
