class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if len(nums)==0:
            return 0
        s=(sorted(set(nums)))
        i=0
        l=[]
        c=1
        while i<len(s)-1:
            if s[i]+1==s[i+1]:
                c+=1
            else:
                l.append(c)
                c=1    
            i+=1 
        l.append(c)    
        return max(l)                   

            

        