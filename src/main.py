from Npuzzle import Board, BoardH
from os import path
from time import time
m = BoardH()

pth = path.abspath("")
pth = pth[:len(pth)-3]+"inst/test3.txt"
m.loadMatrix(pth)
obj = BoardH()
obj.loadMatrix(pth)
print("Pre shuffle")
print(m)
randmoves = 5
m.shuffleInstance(randmoves)
print("random moves : ", randmoves)
print("Pos shuffle")
print(m)

print("A*")
timea = time()
exp, b, d = m.aStar(obj,m)
print("tempo : {}".format((time()-timea)*1000))
print("Ramificação media: {}".format(b))
print("Nós expandidos: ", len(exp))
print("profundidade: {}".format(d))

print("BFS")
timea = time()
exp, b, d = m.bfs(obj,m)
print("tempo : {}".format((time()-timea)*1000))
print("Ramificação media: {}".format(b))
print("Nós expandidos: ", len(exp))
print("profundidade: {}".format(d))

print("DFS")
timea = time()
exp, b, d = m.dfs(obj,m)
print("tempo : {}".format((time()-timea)*1000))
print("Ramificação media: {}".format(b))
print("Nós expandidos: ", len(exp))
print("profundidade: {}".format(d))

# print("IDA*")
# timea = time()
# exp, b, d = m.idaStar(obj,m)
# print("tempo : {}".format((time()-timea)*1000))
# print("Ramificação media: {}".format(b))
# print("Nós expandidos: ", len(exp))
# print("profundidade: {}".format(d))