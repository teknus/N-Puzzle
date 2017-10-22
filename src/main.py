from Npuzzle import Board, BoardH
from os import path
from time import time
m = BoardH()

pth = path.abspath("")
pth = pth[:len(pth)-3]+"inst/test50.txt"
m.loadMatrix(pth)
obj = BoardH()
obj.loadMatrix(pth)
print("Pre shuffle")
print(m)
randmoves = 10
m.shuffleInstance(randmoves)
print("random moves : ", randmoves)
print("Pos shuffle")
print(m)

print("A*")
timea = time()
exp, b = m.aStar(obj,m)
print("tempo : {}".format((time()-timea)*1000))
print("Ramificação media: {}".format(b))

print("IDA*")
timea = time()
exp, b = m.idaStar(obj,m)
print("tempo : {}".format((time()-timea)*1000))
print("Ramificação media: {}".format(b))

print("BFS")
timea = time()
exp, b = m.bfs(obj,m)
print("tempo : {}".format((time()-timea)*1000))
print("Ramificação media: {}".format(b))

#print("DFS")
#exp, b = m.dfs(obj,m)
#print("Ramificação media: {}".format(b))