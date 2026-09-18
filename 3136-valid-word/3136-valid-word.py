class Solution:
    def isValid(self, word: str) -> bool:
        v=False
        c=False
        f=0
        if len(word)>=3:
            for i in word:
                if i.isalnum():
                    f+=1
                    if i in "aeiouAEIOU":
                        v=True
                    if i not in "aeiouAEIOU" and i.isalpha():
                        c=True  
        return v and c and f==len(word)                 

            

        