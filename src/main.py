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
m.shuffleInstance(10)
print(m)
print(obj.actualManhattan)
print(m.actualManhattan)
print(m.manhattanDistanceValue(obj))
# print(m)
# print("BFS")
# exp, b = m.bfs(obj,m)
# print(len(exp),b)
# print()
# print("DFS")
# exp, b = m.dfs(obj,m)
# print(len(exp),b)
