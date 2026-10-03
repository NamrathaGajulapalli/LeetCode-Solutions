class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        d={}
        r=[]
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        s=sorted(d.values())
        s=s[::-1]
        for x in s:
            for i,j in d.items():
                if x==j and i not in r:
                    r.append(i)
                    k-=1
                    if k==0:
                        return r      
     

