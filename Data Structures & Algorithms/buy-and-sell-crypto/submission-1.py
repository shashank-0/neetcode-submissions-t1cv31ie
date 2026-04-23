class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m=0
        i=0
        j=1
        while j<=len(prices)-1:
            if prices[j]>prices[i]:
                m=max(m,prices[j]-prices[i])
                j+=1
            else:
                i=j
                j+=1
        return m

