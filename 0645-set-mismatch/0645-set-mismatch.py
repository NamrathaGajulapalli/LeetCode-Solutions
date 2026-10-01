class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        d={}
        r=[]
        for i in nums:
            if i in d:
                r.append(i)
                break
            else:
                d[i]=1
        for i in range(1,len(nums)+1):
            if i not in nums:
                r.append(i)
                break   
        return r                 

        # nums=sorted(nums)
        # r=[]
        # for i in nums:
        #     if nums.count(i)>1:
        #         r.append(i)
        #         break
        # for i in range(1,len(nums)+1):
        #     if i not in nums:
        #         r.append(i)
        # return r        