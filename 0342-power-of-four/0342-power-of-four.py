class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n<=0:
            return False
        while n%4==0:
            n//=4
        return n==1        
        'it is more time complexity'
        # import math
        # if n>0 and math.log(n,4).is_integer():
        #     return True
        # return False  
        'it is not working:'  
        # if n==1 or n==4:
        #     return True
        # if n==0:
        #     return False    
        # if 4*(n**0.5)==n:
        #     return True
        # return False    
        
                
        