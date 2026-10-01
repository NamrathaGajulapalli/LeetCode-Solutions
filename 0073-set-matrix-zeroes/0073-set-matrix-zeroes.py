class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        r=[]
        c=[]
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j]==0:
                    r.append(i)
                    c.append(j)
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if i in r:
                    matrix[i][j]=0
                if j in c:
                    matrix[i][j]=0              
        """
        Do not return anything, modify matrix in-place instead.
        """
        