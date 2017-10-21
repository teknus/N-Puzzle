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
m.shuffleInstance(2)
print(m)
print(m.actualManhattan)
print(obj.actualManhattan)
print(m.manhattanDistanceValue(obj))
# print(m)
# print("BFS")
# exp, b = m.bfs(obj,m)
# print(len(exp),b)
# print()
# print("DFS")
# exp, b = m.dfs(obj,m)
# print(len(exp),b)
