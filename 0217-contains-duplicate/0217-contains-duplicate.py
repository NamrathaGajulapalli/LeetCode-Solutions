class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # d={}
        # for i in nums:
        #     if i in d:
        #         return True
        #     else:
        #         d[i]=1
        # return False   


        # d=set()     
        # for i in nums:
        #     if i in d:
        #         return True
        #     else:
        #         d.add(i)     
        # return False        
        '''
        if len(set(nums))==len(nums):
            return False
        return True '''
        a=set()
        for i in nums:
            if i in a:
                return True
            else:
                a.add(i)
        return False          
