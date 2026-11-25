class Solution:
    def minimumMoves(self, s: str) -> int:
        i=0
        c=0
        while i<len(s):
            if s[i]=="X":
                c+=1
                i+=3
            else:
                i+=1
        return c            
        
        