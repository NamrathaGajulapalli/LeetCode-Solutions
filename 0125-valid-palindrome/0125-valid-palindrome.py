class Solution:
    def isPalindrome(self, s: str) -> bool:
        r=''
        for i in s:
            if i.isalnum():
                r+=i
        return r.lower()==r[::-1].lower()        


        # l=''
        # for i in s:
        #     if i.isalnum():
        #         l+=i
        # l=l.lower()        
        # le=0
        # r=len(l)-1
        # while le<r:
        #     if l[le]!=l[r]:
        #         return False
        #     le+=1
        #     r-=1  
        # return True      
        'or'

        # l=list(s)
        # r=''
        # g=''
        # for i in range(-1,-len(s)-1,-1):
        #     if l[i].isalnum():
        #         r+=l[i]
        # for i in s:
        #     if i.isalnum():
        #         g+=i
        # return g.lower()==r.lower()      
        'or'

        # l=''
        # a=0
        # b=-1
        # for i in s:
        #     if i.isalnum():
        #         l+=i 
        # x=l.lower()             
        # for i in range(len(x)//2):
        #     if x[i]==x[b]:
        #         b-=1
        #     else:
        #         a=1
        # if a==0:
        #     return True
        # else:
        #     return False                


        