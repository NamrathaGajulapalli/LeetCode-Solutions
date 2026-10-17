class Solution:
    def countAsterisks(self, s: str) -> int:
        c=0
        sc=0
        for i in s:
            if i=='|':
                c+=1    
            if c%2==0:
                if i=='*':
                    sc+=1
        return sc            

        