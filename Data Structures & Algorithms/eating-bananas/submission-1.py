class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        k=max(piles)
        i=1
        j=k
        while i<=j:
            m=(j+i)//2
            t=0
            for l in piles:
                t+=math.ceil(l/m)
            if t>h:
                i=m+1
            else:
                j=m-1
        return j if i<j else i