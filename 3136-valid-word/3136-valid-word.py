class Solution:
    def isValid(self, word: str) -> bool:
        v=0
        c=0
        if len(word)<3:
            return False
        for i in word:
            if i.isalpha():
                if i in 'aeiouAEIOU':
                    v+=1
                else:
                    c+=1
            if not i.isalnum():
                return False
        return v>=1 and c>=1                       
        # v=False
        # c=False
        # f=0
        # if len(word)>=3:
        #     for i in word:
        #         if i.isalnum():
        #             f+=1
        #             if i in "aeiouAEIOU":
        #                 v=True
        #             if i not in "aeiouAEIOU" and i.isalpha():
        #                 c=True  
        # return v and c and f==len(word)                 

            

        