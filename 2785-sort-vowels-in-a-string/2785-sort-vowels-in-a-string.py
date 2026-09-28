class Solution:
    def sortVowels(self, s: str) -> str:
        l=[]
        for i in s:
            if i in "AEIOUaeiou":
                l.append(ord(i))
        l=sorted(l)
        x=0
        r=''
        for i in range(len(s)):
            if s[i] in "AEIOUaeiou":
                r+=chr(l[x])
                x+=1
            else:
                r+=s[i]    
        return r        
                        




        