class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        u=set()
        l=0
        res=0
        for r in range(len(s)):
            while s[r] in u:
                u.remove(s[l])
                l+=1
            res=max(res,r-l+1)
            u.add(s[r])
        return res