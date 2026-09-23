class Solution:
    def diagonalSum(self, mat: list[list[int]]) -> int:
        sumi=0
        for i in range(len(mat)):
            sumi+=mat[i][len(mat)-i-1]
            sumi+=mat[i][i]
        if len(mat)%2==0:
            return sumi
        else:
            return sumi-mat[len(mat)//2][len(mat)//2]        

        