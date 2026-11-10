class Solution:
    def construct2DArray(self, original: list[int], m: int, n: int) -> list[list[int]]:
        if m*n!=len(original):
            return []
        x=[[0]*n for i in range(m)]
        f=0
        for i in range(m):
            for j in range(n):
                x[i][j]=original[f]
                f+=1
        return x          

        