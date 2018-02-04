def setZeroes(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: void Do not return anything, modify matrix in-place instead.
    """
    row = [0] * len(matrix)
    col = [0] * len(matrix[0])


    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                row[i] = 1
                col[j] = 1
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if row[i] == 1 or col[j] == 1:
                matrix[i][j] = 0
matrix=[[1]]
setZeroes(matrix)
print matrix