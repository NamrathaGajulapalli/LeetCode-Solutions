class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        if len(password)<8:
            return False
        l=0
        u=0
        s=0
        d=0
        for i in range(len(password)):
            if i>0 and password[i]==password[i-1]:
                return False
            if password[i].isalpha():
                if password[i]==password[i].upper():
                    u+=1
                else:
                    l+=1
            elif password[i].isdigit():
                d+=1
            else:
                s+=1
        return l>0 and u>0 and d>0 and s>0            



        