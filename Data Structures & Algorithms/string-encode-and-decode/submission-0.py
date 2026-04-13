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
            a=""
            while s[n]!='#':
                a+=s[n]
                n+=1
            n+=1
            a=int(a)
            strs.append(s[n:n+a])
            n+=a
        return strs