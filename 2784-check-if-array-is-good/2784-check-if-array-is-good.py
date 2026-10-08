class Solution:
    def isGood(self, nums: List[int]) -> bool:
        maxi=max(nums)
        r=[]
        for i in range(1,maxi+1):
            r.append(i)
        r.append(maxi)
        return r==sorted(nums)    
        
        