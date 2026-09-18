class Solution:
    def maxFreqSum(self, s: str) -> int:
        d={}
        for i in s:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        v_sum=0
        c_sum=0
        for i,j in d.items():
            if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
                if j>v_sum:
                    v_sum=j
            else:
                if j>c_sum:
                    c_sum=j
        return v_sum+c_sum                             
        