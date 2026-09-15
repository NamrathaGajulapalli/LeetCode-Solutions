class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        r=[]
        f=(len(s)+k-1)//k
        x=''
        for i in s:
            x+=i
            if len(x)==k:
                r.append(x)
                x=""    
        if len(x)>0:
            x+=fill*(k-len(x))
            r.append(x)   
        return r           


        