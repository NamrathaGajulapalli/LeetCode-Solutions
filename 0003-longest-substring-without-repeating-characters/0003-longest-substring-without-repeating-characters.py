class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # r=''
        # maxi=0
        # c=0
        # for i in range(len(s)):
        #     if s[i] not in r:
        #         r+=s[i]
        #         c+=1
        #     else:
        #         r=r[r.index(s[i])+1:]
        #         r+=s[i]
        #         c=len(r)
        #     if maxi<c:
        #         maxi=c
        # return maxi  
        r=[]
        maxi=0
        for i in range(len(s)):
            while s[i] in r:
                r.remove(r[0])
            r.append(s[i])  
            if len(r)>maxi:
                maxi=len(r)
        return maxi                


        




          
