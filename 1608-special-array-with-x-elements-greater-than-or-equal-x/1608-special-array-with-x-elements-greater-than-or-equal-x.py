class Solution:
    def specialArray(self, nums: list[int]) -> int:
        l=[]
        for j in range(1,len(nums)+1):
            c=0
            for i in nums:
                if i>=j:
                    c+=1
            if c==j:
                l.append(j)
        if l:
            return max(l)
        return -1                    
        