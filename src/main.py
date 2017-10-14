from Npuzzle import Board
from os import path

m = Board()
m2 = Board()
pth = path.abspath("")
pth = pth[:len(pth)-3]
m.loadMatrix(pth+"/matrix.txt")
m2.loadMatrix(pth+"/matrix.txt")
m.shuffleInstance(10)
m2.shuffleInstance(2)
m.show()
print(m.possibleMoves)