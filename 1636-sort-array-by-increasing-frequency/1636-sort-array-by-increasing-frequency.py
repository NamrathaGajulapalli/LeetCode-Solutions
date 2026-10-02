class Solution:
    def frequencySort(self, nums: list[int]) -> list[int]:
        s=sorted(nums)
        d={}
        r=[]
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        ds=sorted(d.values())
        for i in ds:
            for k,l in sorted(d.items(),reverse=True):
                if k not in r and l==i:
                    if l==i:
                        r.extend([k]*l)
        return r            

        