from Npuzzle import Board
from os import path

m = Board()

pth = path.abspath("")
pth = pth[:len(pth)-3]
m.loadMatrix(pth+"/matrix.txt")
obj = Board()
obj.loadMatrix(pth+"/matrix.txt")
m.moveDown()
print(m.bfs(obj, m))
