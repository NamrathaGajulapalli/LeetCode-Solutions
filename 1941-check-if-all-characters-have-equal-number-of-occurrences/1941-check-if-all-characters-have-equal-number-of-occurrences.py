class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        d={}
        for i in s:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        a=d[s[0]]       
        for i in d:
            if d[i]!=a:
                return False
                
        return True                 
        