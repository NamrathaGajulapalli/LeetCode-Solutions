class Solution:
    def isHappy(self, n: int) -> bool:
            seen=set()
            while True:
                if n in seen:
                    return False
                seen.add(n) 
                s = 0  
                while n>0: 
                    digit = n % 10
                    s += digit * digit
                    n //= 10
                if n<=0:
                    if s==1:
                        return True
                    n=s
                    s=0
            return False                

                
            

        
# seen = set()  # numbers that already appeared (to detect loop)
        
#         # repeat until we either reach 1 or detect a cycle
# while n != 1 and n not in seen:
#     seen.add(n)
#     n = next_num(n)
        
#     return n == 1
        