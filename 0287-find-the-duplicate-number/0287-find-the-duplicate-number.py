class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        d={}
        for i in nums:
            if i in d:
                return i
            else:
                d[i]=1    
        # d=set()
        # for i in nums:
        #     if i in d:
        #         return i
        #     else:
        #         d.add(i)    