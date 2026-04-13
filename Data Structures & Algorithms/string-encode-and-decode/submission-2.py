class Solution:

    def encode(self, strs: List[str]) -> str:
        s=""
        for i in strs:
            s+=str(len(i))+"#"+i
        return s

    def decode(self, s: str) -> List[str]:
        strs=[]
        n=0
        while n<len(s):
            m=n
            while s[m]!='#':
                m+=1
            a=int(s[n:m])
            strs.append(s[m+1:m+1+a])
            n=m+1+a
        return strs