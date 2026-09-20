class Solution:
    def isPalindromic(self, s: str) -> bool:
        l=[]
        
        for i in s:
            x=''
            x=(bin(ord(i)))[2:].zfill(8)
            for i in x:
                l.append(i)
        x=len(l)-1  
        f=True      
        for i in range(len(l)//2):
            if l[i]!=l[x]:
                f=False
            x-=1
        return f        


        