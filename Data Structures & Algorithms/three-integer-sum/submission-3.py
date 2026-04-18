class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        f=[]
        for i in range(len(nums)-2):
            t=-nums[i]
            if i>0 and nums[i]==nums[i-1]:
                continue
            j=i+1
            k=len(nums)-1
            while j<k:
                l=nums[j]+nums[k]
                if l==t:
                    f.append([-t,nums[j],nums[k]])
                    j+=1
                    while nums[j]==nums[j-1] and j<k:
                        j+=1
                elif l<t:
                    j+=1
                else:
                    k-=1
        return f
