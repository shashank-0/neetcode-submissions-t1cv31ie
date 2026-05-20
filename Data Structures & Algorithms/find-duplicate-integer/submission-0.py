class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        f=set()
        for i in nums:
            if i in f:
                return i
            else:
                f.add(i)