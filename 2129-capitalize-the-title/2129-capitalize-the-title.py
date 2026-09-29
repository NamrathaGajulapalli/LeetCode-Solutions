class Solution:
    def capitalizeTitle(self, title: str) -> str:
        title=title.split(' ')
        r=''
        for i in title:
            if len(i)>2:
                r+=i.capitalize()
            else:
                r+=i.lower()
            r+=' '    
        return r.rstrip()        



        