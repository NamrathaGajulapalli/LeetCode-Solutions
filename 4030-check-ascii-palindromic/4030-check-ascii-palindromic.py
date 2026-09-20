class Solution:
    def isPalindromic(self, s: str) -> bool:
        l=[]
        for i in s:
            x=''
            x=(bin(ord(i)))[2:].zfill(8)
            for i in x:
                l.append(i)
        return l==l[::-1]   

        