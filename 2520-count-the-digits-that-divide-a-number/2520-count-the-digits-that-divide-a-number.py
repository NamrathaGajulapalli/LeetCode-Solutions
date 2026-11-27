class Solution:
    def countDigits(self, num: int) -> int:
        c=0
        temp=num
        while num>0:
            d=num%10
            if temp%d==0:
                c+=1
            num//=10
        return c    
                 
        