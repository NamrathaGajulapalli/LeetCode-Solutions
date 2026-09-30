class Solution:
    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        r=[]
        for i in range(len(matrix[0])):
            x=[]
            for j in range(len(matrix)):
                x.append(matrix[j][i])
            r.append(x)
        return r        
                    
        