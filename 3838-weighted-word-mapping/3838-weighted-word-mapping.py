class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        f=''
        for i in words:
            s=0
            for j in i:
                s+=weights[ord(j)-97]
            r=s%26
            f+=chr(122-r)
        return f  
 
 

                
        