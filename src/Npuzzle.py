#-*- encoding:utf-8 -*-
from random import randint
from os import path
import queue as Q

class Board:
    
    def __init__(self):
        self.instance = list(list())
        self.i0 = 0
        self.j0 = 0
        self.dimension = 0
        self.d = 0
        self.possibleMoves = [0,0,0,0]

    def loadMatrix(self, path):
        with open(path, 'r') as arq:
            lines = arq.readlines()
            tam = int(lines[0])
            matrix = [[0 for x in range(tam)] for y in range(tam)]
            lines = lines[1:]
            i =0 
            for line in lines:
                j=0
                for item in line.split(" "):
                    if item != "\n":
                        if int(item) == 0:
                            self.i0 = i
                            self.j0 = j
                        matrix[i][j] = int(item)
                    else:
                        continue
                    j += 1
                i += 1
            self.instance = matrix
            self.objective = matrix
            self.dimension = tam

    def show(self):
        for line in self.instance:
            print(line)

    def shuffleInstance(self,times):
        while times > 0:
            #up
            if not self.i0 - 1 < 0:
                self.possibleMoves[0] = 1
            #down
            if not self.i0 + 1 == self.dimension:
                self.possibleMoves[1] = 1
            #left
            if not self.j0 - 1 < 0:
                self.possibleMoves[2] = 1
            #right
            if not self.j0 + 1 == self.dimension:
                self.possibleMoves[3] = 1
            move = randint(0,sum(self.possibleMoves)-1)
            while self.possibleMoves[move] == 0:
                move += 1
            self.swap(move)
            times -= 1
    
    def moveUp(self):
        self.instance[self.i0][self.j0] = self.instance[self.i0-1][self.j0]
        self.instance[self.i0-1][self.j0] = 0
        self.i0 -= 1
        self.updatePossibleMoves()
    
    def moveDown(self):
        self.instance[self.i0][self.j0] = self.instance[self.i0+1][self.j0]
        self.instance[self.i0+1][self.j0] = 0
        self.i0 += 1
        self.updatePossibleMoves()
    
    def moveLeft(self):
        self.instance[self.i0][self.j0] = self.instance[self.i0][self.j0-1]
        self.instance[self.i0][self.j0-1] = 0
        self.j0 -= 1
        self.updatePossibleMoves()
    
    def moveRight(self):
        self.instance[self.i0][self.j0] = self.instance[self.i0][self.j0+1]
        self.instance[self.i0][self.j0+1] = 0
        self.j0 += 1
        self.updatePossibleMoves()
    
    def updatePossibleMoves(self):
        #up
        if not self.i0 - 1 < 0:
            self.possibleMoves[0] = 1
        else:
            self.possibleMoves[0] = 0

        #down
        if not self.i0 + 1 == self.dimension:
            self.possibleMoves[1] = 1
        else:
            self.possibleMoves[1] = 0

        #left
        if not self.j0 - 1 < 0:
            self.possibleMoves[2] = 1
        else:
            self.possibleMoves[2] = 0

        #right
        if not self.j0 + 1 == self.dimension:
            self.possibleMoves[3] = 1
        else:
            self.possibleMoves[3] = 0

    def swap(self, moviment):
        if moviment == 0:
            self.moveUp()
        elif moviment == 1:
            self.moveDown()
        elif moviment == 2:
            self.moveLeft()
        elif moviment == 3:
            self.moveRight()

    def copy(self):
        newCopy = Board()
        newCopy.dimension = self.dimension
        newCopy.instance = [[0 for x in range(newCopy.dimension)] for y in range(newCopy.dimension)]
        i = 0
        while i < self.dimension:
            j = 0
            while j < self.dimension:
                newCopy.instance[i][j] = self.instance[i][j]            
                j+=1
            i+=1
        newCopy.i0 = self.i0
        newCopy.j0 = self.j0 
        newCopy.dimension = self.dimension
        newCopy.d = self.d
        newCopy.possibleMoves = self.possibleMoves[:]
        while i < self.dimension:
            j = 0
            while j < self.dimension:
                newCopy.objective[i][j] = self.objective[i][j]            
                j+=1
            i+=1
        return newCopy
    
    def __eq__(self,other):
        i = 0
        while i < self.dimension:
            j = 0
            while j < self.dimension:
               if self.instance[i][j] != other.instance[i][j]:
                   return False
               j += 1
            i += 1
        return True

    def __repr__(self):
        s = "\n\n"
        for i in self.instance:
            s += "|"
            for j in i:
                s += str(j)+" "
            s += "|"
            s += "\n"
        return s[1:]
    
    def __str__(self):
        s = "\n\n"
        for i in self.instance:
            s += "|"
            for j in i:
                s += str(j)+" "
            s += "|"
            s += "\n"
        return s[1:]

    #Hugo
    def bfs(self, targetBoard, actualBoard):
        expandedNodes = []
        NodetoExpand = []
        b = sum(actualBoard.possibleMoves)
        NodetoExpand.append(actualBoard)
        while True:
            if len(NodetoExpand) == 0:
                break          
            nodeToParse = NodetoExpand.pop(0)
            if nodeToParse == targetBoard:
                 return expandedNodes,b, nodeToParse.d
            moves = nodeToParse.possibleMoves[:]
            b = (sum(moves)+b)/2
            expandedNodes.append(nodeToParse)
            index = 0
            while index < 4:
                boardCopy = nodeToParse.copy()
                boardCopy.d = nodeToParse.d + 1
                if moves[index] == 1:
                    if index == 0:                 
                        boardCopy.moveUp()
                    elif index == 1:                   
                        boardCopy.moveDown()
                    elif index == 2:                  
                        boardCopy.moveLeft()
                    elif index == 3:                
                        boardCopy.moveRight()
                if boardCopy not in expandedNodes:
                    if boardCopy not in NodetoExpand:
                        NodetoExpand.append(boardCopy)
                index += 1
    
    #profundidade
    def dfs(self, targetBoard, actualBoard):
        iterator = 0
        while True:
            expandedNodes,b, solved, d = self.dfsL(targetBoard, actualBoard, iterator)
            if solved:
                return expandedNodes, b, d
            iterator += 2
    
    def dfsL(self, targetBoard,actualBoard, dLimit):
        expandedNodes = []
        NodetoExpand = []
        stack = []
        solved = False
        b = sum(actualBoard.possibleMoves)
        NodetoExpand.append([actualBoard,0])
        while True:
            if len(NodetoExpand) == 0:
                if len(stack) > 0:
                    node = stack.pop()
                    NodetoExpand.append(node)
                else:
                    break
            nodeToParse = NodetoExpand.pop()
            if nodeToParse[0] == targetBoard:
                solved = True
                return expandedNodes, b, solved, nodeToParse[0].d
            moves = nodeToParse[0].possibleMoves[:]
            b = (sum(moves)+b)/2
            expandedNodes.append(nodeToParse[0])
            index = nodeToParse[1]
            while index < 4:
                boardCopy = nodeToParse[0].copy()
                boardCopy.d = nodeToParse[0].d + 1
                if(moves[index] == 1):
                    if index == 0:                 
                        boardCopy.moveUp()
                    elif index == 1:                   
                        boardCopy.moveDown()
                    elif index == 2:                  
                        boardCopy.moveLeft()
                    elif index == 3:                
                        boardCopy.moveRight()
                    if boardCopy not in expandedNodes:
                        if boardCopy not in NodetoExpand:
                            if not boardCopy.d > dLimit:
                                NodetoExpand.append([boardCopy,0])
                                stack.append([nodeToParse[0].copy(),index])
                        break
                index += 1 
        return expandedNodes, b, solved ,0

class BoardH(Board):
    def __init__(self):
        Board.__init__(self)
        self.actualManhattan = dict()
        self.d = 0
        self.h = 0

    def loadMatrix(self, path):
        with open(path, 'r') as arq:
            lines = arq.readlines()
            tam = int(lines[0])
            matrix = [[0 for x in range(tam)] for y in range(tam)]
            lines = lines[1:]
            i =0 
            for line in lines:
                j=0
                for item in line.split(" "):
                    if item != "\n":
                        if int(item) == 0:
                            self.i0 = i
                            self.j0 = j
                        matrix[i][j] = int(item)
                    else:
                        continue
                    j += 1
                i += 1
            self.instance = matrix
            self.objective = matrix
            self.dimension = tam
            self.findAll()

    def find(self,n):
        i = 0
        for line in self.instance:
            j =0 
            for item in line:
                if item == n:
                    return i,j
                j += 1
            i += 1

    def manhattanDistance(self, obj, actual):
        if obj[0] == actual[0] and obj[1] == actual[1]:
            return 0
        return abs((obj[0] - actual[0])) + abs((obj[1]-actual[1]))
    
    def manhattanDistanceValue(self, targetBoard):
        i = (self.dimension * self.dimension) - 1
        value = 0
        while i >= 0:
            l = self.manhattanDistance(self.actualManhattan[i],targetBoard.actualManhattan[i])
            value += l
            i -= 1
        self.h = value          

    def findAll(self):
        i = 0
        roof = (self.dimension * self.dimension)
        while i < roof:
            self.actualManhattan[i] = self.find(i)
            i += 1

    def shuffleInstance(self,times):
        while times > 0:
            #up
            if not self.i0 - 1 < 0:
                self.possibleMoves[0] = 1
            #down
            if not self.i0 + 1 == self.dimension:
                self.possibleMoves[1] = 1
            #left
            if not self.j0 - 1 < 0:
                self.possibleMoves[2] = 1
            #right
            if not self.j0 + 1 == self.dimension:
                self.possibleMoves[3] = 1
            move = randint(0,sum(self.possibleMoves)-1)
            while self.possibleMoves[move] == 0:
                move += 1
            self.swap(move)
            times -= 1
        self.findAll()
    
    def updatePossibleMoves(self):
        #up
        if not self.i0 - 1 < 0:
            self.possibleMoves[0] = 1
        else:
            self.possibleMoves[0] = 0

        #down
        if not self.i0 + 1 == self.dimension:
            self.possibleMoves[1] = 1
        else:
            self.possibleMoves[1] = 0

        #left
        if not self.j0 - 1 < 0:
            self.possibleMoves[2] = 1
        else:
            self.possibleMoves[2] = 0

        #right
        if not self.j0 + 1 == self.dimension:
            self.possibleMoves[3] = 1
        else:
            self.possibleMoves[3] = 0
        self.findAll()

    def copy(self):
        newCopy = BoardH()
        newCopy.dimension = self.dimension
        newCopy.instance = [[0 for x in range(newCopy.dimension)] for y in range(newCopy.dimension)]
        i = 0
        while i < self.dimension:
            j = 0
            while j < self.dimension:
                newCopy.instance[i][j] = self.instance[i][j]            
                j+=1
            i+=1
        newCopy.i0 = self.i0
        newCopy.j0 = self.j0 
        newCopy.dimension = self.dimension
        newCopy.d = self.d
        newCopy.possibleMoves = self.possibleMoves[:]
        newCopy.actualManhattan = self.actualManhattan
        while i < self.dimension:
            j = 0
            while j < self.dimension:
                newCopy.objective[i][j] = self.objective[i][j]            
                j+=1
            i+=1
        return newCopy
    
    def __eq__(self,other):
        i = 0
        while i < self.dimension:
            j = 0
            while j < self.dimension:
               if self.instance[i][j] != other.instance[i][j]:
                   return False
               j += 1
            i += 1
        return True

    def __lt__(self,other):
        return self.h < other.h
        
    def aStar(self, targetBoard,actualBoard):
        expandedNodes = []
        b = sum(actualBoard.possibleMoves)
        NodetoExpand = Q.PriorityQueue()
        NodetoExpand.put((actualBoard.h,actualBoard))
        while True:
            if NodetoExpand.empty():
                break          
            nodeToParse = NodetoExpand.get()
            if nodeToParse[1] == targetBoard:
                return expandedNodes,b, nodeToParse[1].d
            moves = nodeToParse[1].possibleMoves[:]
            b = (sum(moves)+b)/2
            expandedNodes.append(nodeToParse[1])
            index = 0
            while index < 4:
                boardCopy = nodeToParse[1].copy()
                boardCopy.d = nodeToParse[1].d + 1
                if moves[index] == 1:
                    if index == 0:                 
                        boardCopy.moveUp()
                    elif index == 1:                   
                        boardCopy.moveDown()
                    elif index == 2:                  
                        boardCopy.moveLeft()
                    elif index == 3:                
                        boardCopy.moveRight()
                if boardCopy not in expandedNodes:
                    temp = []
                    while not NodetoExpand.empty():
                        temp.append(NodetoExpand.get()[1])
                    if boardCopy not in temp:
                        boardCopy.manhattanDistanceValue(targetBoard)
                        NodetoExpand.put((boardCopy.h,boardCopy))
                    for item in temp:
                        NodetoExpand.put((item.h,item))
                index += 1
    
    def idaStar(self, targetBoard, actualBoard):
        actualBoard.manhattanDistanceValue(targetBoard)
        nos = Q.PriorityQueue()
        limit = actualBoard.h
        while True:
            expandedNodes, b, solved, limit, d = self.idaDoThis(targetBoard, actualBoard, limit)
            if solved:
                return expandedNodes, b, d

    
    def idaDoThis(self, targetBoard, actualBoard, dLimit):
        expandedNodes = []
        b = sum(actualBoard.possibleMoves)
        NodetoExpand = Q.PriorityQueue()
        NodeNotExpand = Q.PriorityQueue()
        NodetoExpand.put((actualBoard.h,actualBoard))
        solved = False
        while True:
            if NodetoExpand.empty():
                n = NodeNotExpand.get()
                limit = n[0] + dLimit
                while limit < dLimit:
                    limit = n[0] + dLimit
                    NodeNotExpand.put(n)
                return expandedNodes,b,False,limit,nodeToParse[1].d      
            nodeToParse = NodetoExpand.get()
            
            if nodeToParse[1] == targetBoard:
                return expandedNodes,b,True,0,nodeToParse[1].d
            moves = nodeToParse[1].possibleMoves[:]
            b = (sum(moves)+b)/2
            expandedNodes.append(nodeToParse[1])
            index = 0
           
            while index < 4:
                boardCopy = nodeToParse[1].copy()
                boardCopy.d = nodeToParse[1].d + 1
                if moves[index] == 1:
                    if index == 0:                 
                        boardCopy.moveUp()
                    elif index == 1:                   
                        boardCopy.moveDown()
                    elif index == 2:                  
                        boardCopy.moveLeft()
                    elif index == 3:                
                        boardCopy.moveRight()
                if boardCopy not in expandedNodes:
                    temp = []
                    while not NodetoExpand.empty():
                        temp.append(NodetoExpand.get()[1])
                    if boardCopy not in temp:
                        boardCopy.manhattanDistanceValue(targetBoard)
                        if boardCopy.h < dLimit:
                            NodetoExpand.put((boardCopy.h,boardCopy))
                        else:
                            NodeNotExpand.put((boardCopy.h,boardCopy))
                    for item in temp:
                        NodetoExpand.put((item.h,item))
                index += 1
#Guardar a profundidade junto com o nó na lista de nós para expandir
