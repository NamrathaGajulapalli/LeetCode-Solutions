class Solution:
    def isValid(self, s: str) -> bool: 
        if len(s)%2!=0:
            return False
        r=[]
        d={'(':')','[':']','{':'}'}
        for i in s:
            if i in '({[':
                r.append(i)
            elif r and i==d[r[-1]]:
                r.pop()
            else:
                return False
        if r:
            return False
        return True                   
