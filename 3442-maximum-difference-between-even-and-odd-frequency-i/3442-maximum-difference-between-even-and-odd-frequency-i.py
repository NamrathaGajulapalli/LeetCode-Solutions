class Solution:
    def maxDifference(self, s: str) -> int:
        d={}
        e=float('inf')
        o=0
        for i in s:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for i in d:
            if d[i]%2==0:
                if d[i]<e:
                    e=d[i]
            else:
                if d[i]>o:
                    o=d[i]      
        return o-e         


        