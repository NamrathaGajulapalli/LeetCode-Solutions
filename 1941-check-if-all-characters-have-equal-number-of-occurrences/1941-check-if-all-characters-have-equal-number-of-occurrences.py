class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        d={}
        for i in s:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        a=set()        
        for i in d:
            a.add(d[i])
        return len(a)==1                
        