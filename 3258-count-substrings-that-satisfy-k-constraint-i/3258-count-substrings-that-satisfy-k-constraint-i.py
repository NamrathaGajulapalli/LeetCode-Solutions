class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        l=[]
        c=0
        for i in range(len(s)):
            x=[]
            for j in range(i+1,len(s)+1):
                x.append(s[i:j])
            l.append(x)    
        for i in l:
            for j in i:
                if j.count('0')<=k or j.count('1')<=k:
                    c+=1
        return c    
        
                
        