class Solution:
    def sortVowels(self, s: str) -> str:
        l=[]
        for i in s:
            if i in "AEIOUaeiou":
                l.append(i)
        l=sorted(l)
        x=0
        r=''
        for i in s:
            if i in "AEIOUaeiou":
                r+=l[x]
                x+=1
            else:
                r+=i    
        return r        
                        




        