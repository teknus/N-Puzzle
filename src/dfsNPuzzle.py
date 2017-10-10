from skeletonNPuzzle import Matrix
from os import path

m = Matrix()
pth = path.abspath("")
pth = pth[:len(pth)-3]
m.loadMatrix(pth+"/matrix.txt")
m.shuffleInstance(8)
m.show()