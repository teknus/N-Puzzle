from skeletonNPuzzle import Matrix
from os import path

m = Matrix()
m2 = Matrix()
pth = path.abspath("")
pth = pth[:len(pth)-3]
m.loadMatrix(pth+"/matrix.txt")
m2.loadMatrix(pth+"/matrix.txt")
# m.shuffleInstance(8)
# m2.shuffleInstance(8)
m.show()
print()
m2.show()
print(m == m2)