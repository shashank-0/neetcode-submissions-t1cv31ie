class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        f={}
        for i in nums:
            if i not in f:
                f[i]=1
            else:
                f[i]+=1
        t=sorted(f.items(), key=lambda x: x[1],reverse=True)
        t=t[:k]
        l=[]
        for (a,b) in t:
            l.append(a)
        return l