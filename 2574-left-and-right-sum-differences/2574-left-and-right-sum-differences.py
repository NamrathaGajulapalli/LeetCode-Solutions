class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        lsum=[0]
        rsum=[0]
        s=0
        for i in nums:
            if len(lsum)==len(nums):
                break
            s+=i
            lsum.append(s)
        s=0
        for i in nums[::-1]:
            if len(rsum)==len(nums):
                break
            s+=i
            rsum.append(s)
        r=[]
        rsum=rsum[::-1]
        print(lsum,rsum)
        for i in range(len(nums)):
            r.append(abs(lsum[i]-rsum[i]) ) 
        return r      

        