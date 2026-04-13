class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        tp=1
        c=0
        for i in nums:
            if i==0:
                c+=1
                continue
            tp*=i
        f=[]
        if c==0:
            for j in nums:
                f.append(int(tp/j))
        elif c==1:
            for j in nums:
                if j==0:
                    f.append(tp)
                else:
                    f.append(0)
        else:
            f=[0]*len(nums)
        return f