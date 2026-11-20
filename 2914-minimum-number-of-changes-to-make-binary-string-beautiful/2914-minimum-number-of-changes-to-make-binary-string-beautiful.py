class Solution:
    def minChanges(self, s: str) -> int:
        i=1
        c=0
        while i<len(s):
            if s[i-1]!=s[i]:
                c+=1
            i+=2
        return c  
   
                  
               
        