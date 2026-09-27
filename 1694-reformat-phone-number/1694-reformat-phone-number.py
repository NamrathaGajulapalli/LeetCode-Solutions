class Solution:
    def reformatNumber(self, number: str) -> str:
        a=''
        r=''
        for i in number:
            if i!='-' and i!=' ':
                a+=i
        x=len(a)
        i=0
        while x>4:
            r+=a[i:i+3]
            r+='-'
            i+=3
            x-=3
        if x==4:
            r+=a[i:i+2]
            r+='-'
            i=i+2
            x-=2
            r+=a[i:i+2]
            i=i+2
            x-=2
        elif x<=3:
            r+=a[i:i+x]
            x=0
        return r                






        