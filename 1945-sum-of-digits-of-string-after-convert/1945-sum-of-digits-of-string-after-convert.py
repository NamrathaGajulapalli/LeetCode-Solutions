class Solution:
    def getLucky(self, s: str, k: int) -> int:
        a=''
        for i in s:
            a+=str(ord(i)-96)
        sumi=0    
        i=0 
        while i<k:
            sumi=0
            for j in a:
                sumi+=int(j)   
            a=str(sumi )  
            i+=1 
        return sumi    
       
              
   
           
            

           

        