class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace('.','[.]')
        # r=''
        # for i in address:
        #     if i=='.':
        #         r+='[.]'
        #     else:
        #         r+=i   
        # return r         
        
