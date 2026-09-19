class Solution:
    def modifyString(self, s: str) -> str:
        l=list(s)
        x=['a','b','c']
        for i in range(len(l)):
            if l[i]=='?':
                for j in x:
                    if i>0 and l[i-1]==j:
                        continue
                    if i<len(l)-1 and l[i+1]==j:
                        continue
                    l[i]=j
        return "".join(l)                    
                   
                        




                    
               



        