class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        r=''
        maxi=0
        c=0
        for i in range(len(s)):
            if s[i] not in r:
                r+=s[i]
                c+=1
            else:
                r=r[r.index(s[i])+1:]
                r+=s[i]
                c=len(r)
            if maxi<c:
                maxi=c
        return maxi        


        




          
