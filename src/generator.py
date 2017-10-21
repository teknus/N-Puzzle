dim = 3
instance = [[]]

i = 0
index = 1
matrix = [[0 for x in range(dim)]for y in range(dim)]
while i < dim:
    j = 0
    while j < dim:
        matrix[i][j] = index
        index += 1
        j += 1
    i += 1
matrix[dim-1][dim-1] = 0
instance = matrix

for line in instance:
		print (line)
        