class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        import math
        if n>0 and math.log(n,4).is_integer():
            return True
        return False    
        # if n==1 or n==4:
        #     return True
        # if n==0:
        #     return False    
        # if 4*(n**0.5)==n:
        #     return True
        # return False    
        
                
        