from skeletonNPuzzle import Matrix
from os import path

m = Matrix()
m2 = Matrix()
pth = path.abspath("")
pth = pth[:len(pth)-3]
m.loadMatrix(pth+"/matrix.txt")
m2.loadMatrix(pth+"/matrix.txt")
m.shuffleInstance(1)
m2.shuffleInstance(2)
m.show()
print(m.possibleMoves)