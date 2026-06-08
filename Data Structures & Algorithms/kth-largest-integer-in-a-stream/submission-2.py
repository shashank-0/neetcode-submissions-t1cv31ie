class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.stream=sorted(nums, reverse=True)
        self.kth=k-1
        self.l=len(nums)


    def add(self, val: int) -> int:
        i=0
        j=self.l
        m=0
        while i<j:
            m=(i+j)//2
            if val>self.stream[m]:
                j=m
            else:
                i=m+1
        self.stream.insert(i,val)
        self.l+=1
        return self.stream[self.kth]