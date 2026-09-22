class Solution:
    def check(self, nums: list[int]) -> bool:
        s=sorted(nums)
        for i in range(len(s)):
            s.append(s.pop(0))
            if s==nums:
                return True
        return False        
                   

        