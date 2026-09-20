class Solution:
    def minimumFlips(self, n: int) -> int:
        b=bin(n)[2:]
        r=b[::-1]
        x=0
        for i in range(len(b)):
            if b[i]!=r[i]:
                x+=1
        return x        
