class Solution:
    def checkString(self, s: str) -> bool:
        return 'ba' not in s
        #it's my code:
        # x=0
        # if len(s)==s.count('a'):
        #     return True
        # for i in range (-1,-len(s),-1):
        #     if s[i]=='b':
        #         x=len(s)+i
        # for i in range(len(s)):
        #     if s[i]=='a':
        #         if i>x:
        #             return False            
        # return True            

        