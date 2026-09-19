class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if len(nums)==0:
            return 0
        s=(sorted(set(nums)))
        i=0
        maxi=0
        c=1
        while i<len(s)-1:
            if s[i]+1==s[i+1]:
                c+=1
            else:
                if maxi<c:
                    maxi=c
                c=1    
            i+=1 
        if maxi<c:
            maxi=c    
        return maxi                   

            

        