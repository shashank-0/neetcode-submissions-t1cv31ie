class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        h=set(nums)
        m=0
        for i in h:
            n=1
            if i-1 in h:
                continue
            else:
                j=i
                while j+1 in h:
                    n+=1
                    j+=1
            if n>m:
                m=n
        return m