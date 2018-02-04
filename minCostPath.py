import sys
def minPathSum(grid,m,n):
    """
    :type grid: List[List[int]]
    :rtype: int
    """


    if m < 0 or n < 0:
        return sys.maxsize
    elif m == 0 and n == 0:
        return grid[m][n]
    else:
        return grid[m][n] + min(minPathSum(grid,m,n-1), minPathSum(grid,m-1,n))


grid=[[1,2,5],[3,2,1]]
m = len(grid) - 1
n=len(grid)-1
print minPathSum(grid,m,n)


"""DP SOLTUTION"""


def minCost(cost, m, n):

    tc = [[0 for x in range(C)] for x in range(R)]

    tc[0][0] = cost[0][0]

    # Initialize first column of total cost(tc) array
    for i in range(1, m + 1):
        tc[i][0] = tc[i - 1][0] + cost[i][0]

    # Initialize first row of tc array
    for j in range(1, n + 1):
        tc[0][j] = tc[0][j - 1] + cost[0][j]

    # Construct rest of the tc array
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            tc[i][j] = min(tc[i - 1][j - 1], tc[i - 1][j], tc[i][j - 1]) + cost[i][j]

    return tc[m][n]