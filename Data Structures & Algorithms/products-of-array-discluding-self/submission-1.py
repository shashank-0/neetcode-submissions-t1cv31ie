class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        f=[nums[0]]
        b=[nums[-1]]
        n=len(nums)
        for i in range(1,n):
            f.append(nums[i]*f[i-1])
            b.append(nums[n-1-i]*b[i-1])
        b.reverse()
        t=[b[1]]
        for i in range(1,n-1):
            t.append(f[i-1]*b[i+1])
        t.append(f[n-2])
        return t