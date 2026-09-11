class Solution:
    def reverseBits(self, n: int) -> int:
        b=bin(n)[2:].zfill(32)
        r=b[::-1]
        return int(r,2)
        
        
        