class Solution:
    def arrayRankTransform(self, arr: list[int]) -> list[int]:
        s=sorted(set(arr))
        d={}
        m=1
        for i in s:
            d[i]=m
            m+=1
        r=[]
        for i in arr:
            r.append(d[i])
        return r        

        