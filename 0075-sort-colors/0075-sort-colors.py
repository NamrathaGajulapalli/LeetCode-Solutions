class Solution:
    def sortColors(self, nums: List[int]) -> None:
        # for i in range(len(nums)):
        #     for j in range(0,len(nums)-i-1):
        #         if nums[j]>nums[j+1]:
        #             nums[j+1],nums[j]=nums[j],nums[j+1]
        c0=0
        c1=0
        c2=0
        for i in nums:
            if i==0:
                c0+=1
            if i==1:
                c1+=1
            if i==2:
                c2+=1
        index=0
        for i in range(c0):
            nums[index]=0
            index+=1      
        for i in range(c1):
            nums[index]=1
            index+=1
        for i in range(c2):
            nums[index]=2
            index+=1    
 
   
        # for i in range(c2):
        #     nums[index]=2
        #     index+=1 
     
        # return nums                   

        

        """
        Do not return anything, modify nums in-place instead.
        """
        