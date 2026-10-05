class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        word=sorted(set(word))
        c=0
        for i in word:
            if i.lower() in word and i.upper() in word:
                c+=1
        return c//2        
            
        




        