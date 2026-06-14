class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        f=Counter(tasks)

        mf=max(f.values())
        mc=sum(1 for i in f.values() if i==mf)
        return max(len(tasks),(mf-1)*(n+1)+mc)