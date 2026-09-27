class Solution:
    def sumZero(self, n: int) -> list[int]:
        a=[]
        i=0
        x=-(n//2)
        if n%2!=0:
            while i<n:
                a.append(x)
                x+=1
                i+=1
        else:
            while i<n:
                if x==0:
                    x+=1
                    continue
                a.append(x)
                x+=1
                i+=1
        return a

        