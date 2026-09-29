class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        x=len(s)
        a=s[:x//2]
        b=s[x//2:]
        v1=0
        v2=0
        for i in range(len(a)):
            if a[i] in "AEIOUaeiou":
                v1+=1
            if b[i] in "AEIOUaeiou":
                v2+=1
        return v1==v2            

        