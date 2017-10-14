#Skeleton
from random import randint

class Board:
    
    def __init__(self):
        self.instance = list(list())
        self.i0 = 0
        self.j0 = 0
        self.dimension = 0
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
                    if int(item) == 0:
                        self.i0 = i
                        self.j0 = j
                    matrix[i][j] = int(item)
                    j += 1
                i += 1
            self.instance = matrix
            self.dimension = tam
        
    def show(self):
        for line in self.instance:
            print(line)

    def shuffleInstance(self,times):
        while times > 0:
            self.updatePossibleMoves()
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
