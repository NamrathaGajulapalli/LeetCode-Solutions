class Solution:
    def mostFrequent(self, nums: list[int], key: int) -> int:
        d={}
        maxi=0
        t=0
        for i in range(len(nums)-1):
            if nums[i]==key:
                if nums[i+1] in d:
                    d[nums[i+1]]+=1
                else:
                    d[nums[i+1]]=1
        for i in d:
            if d[i]>maxi:
                maxi=d[i] 
                t=i               
                
        return t             






        