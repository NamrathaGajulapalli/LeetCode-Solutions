class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        p=[]
        n=[]
        r=[]
        for i in nums:
            if i>0:
                p.append(i)
            else:
                n.append(i)
        for i in range(len(p)):
            r.append(p[i])
            r.append(n[i])
        return r    

        