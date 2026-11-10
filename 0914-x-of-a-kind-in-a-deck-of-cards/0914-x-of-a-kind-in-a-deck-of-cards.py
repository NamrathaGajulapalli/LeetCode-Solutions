class Solution:
    def hasGroupsSizeX(self, deck: list[int]) -> bool:
        d={}
        for i in deck:
            if i in d:
                d[i]+=1
            else:
                d[i]=1       
        h=d.values()
        for i in range(2,max(h)+1):
            k=0
            for j in h:
                if j%i==0:
                    k+=1
            if k==len(h) and i>=2:
                return True
        return False        



        