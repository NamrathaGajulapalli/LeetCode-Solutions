class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        r=[]
        for i in range(numRows):
            r.append([1]*(i+1))
        for i in range(2,numRows):
            for j in range(1,i): 
                r[i][j]=r[i-1][j]+r[i-1][j-1]
        return r           

            


        