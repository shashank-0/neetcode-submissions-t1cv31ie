class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        f=[0]*len(temperatures)
        s=[]
        for i,t in enumerate(temperatures):
            while s and s[-1][0]<t:
                st,si=s.pop()
                f[si]=i-si
            s.append([t,i])
        return f