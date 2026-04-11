class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        for i in nums:
            d[i]=1+d.get(i,0)
        l=[[] for i in range(len(nums)+1)]
        for j,o in d.items():
            l[o].append(j)
        f=[]
        for m in range(len(l)-1,0,-1):
            for n in l[m]:
                f.append(n)
                if len(f)==k:
                    return f