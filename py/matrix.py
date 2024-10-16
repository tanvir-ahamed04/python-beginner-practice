matrix1 = [[12, 7, 3],
           [4, 5, 6],
           [7, 8, 9]]

matrix2 = [[5, 8, 1],
           [6, 7, 3],
           [4, 5, 9]]

result = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]

for i in range(3):
    for j in range(3):
        result[i][j] = matrix1[i][j] + matrix2[i][j]

for row in result:
    print(row)