class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        s='abcdefghijklmnopqrstuvwxyz'
        x=sorted(set(sentence))
        return s==''.join(x)
        # d={}
        # for i in sentence:
        #     if i in d:
        #         d[i]+=1
        #     else:
        #         d[i]=1
        # if len(d)==26:
        #     return True
        # return False                

        