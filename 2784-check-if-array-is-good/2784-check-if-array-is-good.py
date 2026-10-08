class Solution:
    def isGood(self, nums: List[int]) -> bool:
        maxi=max(nums)
        if len(nums)!=maxi+1:
            return False
        r=[]
        for i in range(1,maxi+1):
            r.append(i)
        r.append(maxi)
        return r==sorted(nums)    
        
        