class Solution:
    def isOneBitCharacter(self, bits: list[int]) -> bool:
        i=0
        while i<len(bits):
            if i==len(bits)-1 and bits[i]==0:
                return True
            if bits[i]==0:
                i+=1
            else:
                i+=2 
        return False          


               
        