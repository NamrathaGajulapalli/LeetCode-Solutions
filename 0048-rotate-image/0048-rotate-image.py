class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        r=[]
        for i in range(len(matrix)):
            x=[]
            for j in range(len(matrix[i])):
                x.append(matrix[j][i])
            r.append(x[::-1])
        for i in range(len(r)):
            matrix[i]=r[i]      


        # for i in range(len(matrix)):
        #     for j in range(i+1,len(matrix[i])):
        #         matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        # for i in range(len(matrix)):
        #     matrix[i]=matrix[i][::-1]
        """
        Do not return anything, modify matrix in-place instead.
        """
        