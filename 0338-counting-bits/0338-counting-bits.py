class Solution:
    def countBits(self, n: int) -> List[int]:
        l=[0]*(n+1)
        for i in range(1,n+1):
            bit=[]
            x=i
            while x>0:
                bit.append(x%2)
                x//=2
            c=0    
            for j in bit:
                if j==1:
                    c+=1
            l[i]=c       
        return l    


        