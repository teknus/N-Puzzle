#Skeleton
from random import randint

class Matrix:
    
    def __init__(self):
        self.instance = list(list())
        self.i0 = 0
        self.j0 = 0
        self.dimension = 0

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
                    matrix[i][j] = int(item)
                    j += 1
                i += 1
            self.instance = matrix
            self.findZero()
            self.dimension = tam
        
    def show(self):
        for line in self.instance:
            print(line)

    def findZero(self):
        self.i0 = 0
        for line in self.instance:
            self.j0 = 0
            for number in line:
                if number == 0:
                    return
                self.j0 += 1
            self.i0 += 1

    def shuffleInstance(self,times):
        while times > 0:
            possibleMoves = [0,0,0,0]
            #up
            if not self.i0 - 1 < 0:
                possibleMoves[0] = 1
            #down
            if not self.i0 + 1 == self.dimension:
                possibleMoves[1] = 1
            #left
            if not self.j0 - 1 < 0:
                possibleMoves[2] = 1
            #right
            if not self.j0 + 1 == self.dimension:
                possibleMoves[3] = 1
            move = randint(0,sum(possibleMoves)-1)
            while possibleMoves[move] == 0:
                move += 1
            self.swap(move)
            times -= 1

    def swap(self, moviment):
        if moviment == 0:
            self.instance[self.i0][self.j0] = self.instance[self.i0-1][self.j0]
            self.instance[self.i0-1][self.j0] = 0
            self.i0 -= 1
        elif moviment == 1:
            self.instance[self.i0][self.j0] = self.instance[self.i0+1][self.j0]
            self.instance[self.i0+1][self.j0] = 0
            self.i0 += 1
        elif moviment == 2:
            self.instance[self.i0][self.j0] = self.instance[self.i0][self.j0-1]
            self.instance[self.i0][self.j0-1] = 0
            self.j0 -= 1
        elif moviment == 3:
            self.instance[self.i0][self.j0] = self.instance[self.i0][self.j0+1]
            self.instance[self.i0][self.j0+1] = 0
            self.j0 += 1
    
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
