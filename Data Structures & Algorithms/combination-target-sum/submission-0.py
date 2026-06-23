class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]

        sub=[]
        def back(i,sum):
            if sum==target:
                res.append(sub.copy())
            elif sum>target or i>=len(nums):
                return
            else:
                sub.append(nums[i])
                back(i,sum+nums[i])
                sub.pop()
                back(i+1,sum)
        
        back(0,0)
        return res