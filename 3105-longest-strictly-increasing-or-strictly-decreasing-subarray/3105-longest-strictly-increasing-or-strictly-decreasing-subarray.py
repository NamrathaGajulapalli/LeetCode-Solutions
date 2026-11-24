class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        ic=1
        lic=[1]
        dc=1
        ldc=[1]
        for i in range(len(nums)-1):
            if nums[i]<nums[i+1]:
                ic+=1
            else:
                lic.append(ic)
                ic=1
            if nums[i]>nums[i+1]:
                dc+=1
            else:
                ldc.append(dc)
                dc=1
        lic.append(ic)
        ldc.append(dc) 
        return max(max(lic),max(ldc))       
           


        
        