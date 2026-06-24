class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        l=len(nums)
        def back(sub,t):
            if not t:
                res.append(sub[:])
                return
            else:
                for j in list(t):
                    sub.append(j)
                    t.remove(j)
                    back(sub,t)
                    sub.pop()
                    t.add(j)

        back([],set(nums))
        return res