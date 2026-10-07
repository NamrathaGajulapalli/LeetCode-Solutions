class Solution:
    def countCharacters(self, words: list[str], chars: str) -> int:
        r=0
        for i in words:
            temp=chars
            f=True
            for j in i:
                if j not in temp:
                    f=False
                else:
                    temp=temp.replace(j,'',1)
            if f==True:
                r+=len(i)         
            
        return r        

        