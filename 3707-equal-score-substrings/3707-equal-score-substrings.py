class Solution:
    def scoreBalance(self, s: str) -> bool:
        t=0
        for i in s:
            t+=ord(i)-96
        l=0    
        for i in s:
            l+=ord(i)-96
            if l==t-l:
                return True
        return False        

            
            

        # if len(s)%2==0:
        #     x=len(s)//2
        # else:
        #     x=int((len(s)//2)+1)    
        # s1=0
        # s2=0
        # for i in range(x):
        #     s1+=ord(s[i])-96
        # for i in range(x,len(s)):
        #     s2+=ord(s[i])-96
        # if s1==s2:
        #     return True
        # else:
        #     return False

        