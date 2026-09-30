class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        r=[]
        if rowIndex==0:
            return [1]
        if rowIndex==1:
            return [1,1]    
        for i in range(rowIndex+1):
            r.append([1]*(i+1))
        for i in range(2,rowIndex+1):
            for j in range(1,i):
                r[i][j]=r[i-1][j]+r[i-1][j-1]
        return r[-1]        

        