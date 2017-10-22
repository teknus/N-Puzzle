from Npuzzle import Board, BoardH
from os import path

m = BoardH()

pth = path.abspath("")
pth = pth[:len(pth)-3]+"inst/test50.txt"
m.loadMatrix(pth)
obj = BoardH()
obj.loadMatrix(pth)
print("Pre shuffle")
print(m)
randmoves = 3
m.shuffleInstance(randmoves)
print("random moves : ", randmoves)
print("Pos shuffle")
print(m)
#print("A*")
#exp, b = m.aStar(obj,m)
#print(len(exp),b)
#print("IDA*")
#exp, b = m.IDA(obj,m)
#print(len(exp),b)

#print("BFS")
#exp, b = m.bfs(obj,m)
#print(len(exp),b)

print("DFS")
exp, b = m.dfs(obj,m)
print(len(exp),b)