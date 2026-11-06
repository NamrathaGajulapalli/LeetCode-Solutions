class Solution:
    def kthDistinct(self, arr: list[str], k: int) -> str:
        d={}
        c=0
        for i in arr:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for i,j in d.items():
            if j==1:
                c+=1 
            if c==k:
                return i
        return ""                      
        