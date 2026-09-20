class Solution:
    def generateTag(self, caption: str) -> str:
        r='#'
        l=list((caption.lstrip()).split(' '))
        for i in range(len(l)):
            if i==0:
                r+=l[i].lower()
            else:    
                r+=l[i].title()    
        return r[:100]        
            
        