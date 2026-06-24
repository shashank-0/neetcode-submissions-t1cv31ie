class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        candidates.sort()
        def back(i,sum,sub):
            if sum==target:
                res.append(sub.copy())
                return
            elif i==len(candidates) or sum>target:
                return
            else:
                sub.append(candidates[i])
                back(i+1,sum+candidates[i],sub)

                while i+1<len(candidates) and candidates[i]==candidates[i+1]:
                    i+=1
                sub.pop()
                back(i+1,sum,sub)
        
        back(0,0,[])
        return res