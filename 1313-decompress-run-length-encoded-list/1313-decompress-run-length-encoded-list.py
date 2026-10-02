class Solution:
    def decompressRLElist(self, nums: list[int]) -> list[int]:
        r=[]
        for i in range(0,len(nums),2):
            r.extend([nums[i+1]]*nums[i])
        return r    
            

        