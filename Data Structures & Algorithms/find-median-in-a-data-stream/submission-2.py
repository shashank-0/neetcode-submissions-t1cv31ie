class MedianFinder:

    def __init__(self):
        self.l=[]
        self.r=[]

    def addNum(self, num: int) -> None:
        if len(self.r)==0:
            heapq.heappush(self.r,num)
        elif len(self.l)<len(self.r):
            if num<=self.r[0]:
                heapq.heappush(self.l,-num)
            else:
                t=heapq.heappushpop(self.r,num)
                heapq.heappush(self.l,-t)
        else:
            if num>=-self.l[0]:
                heapq.heappush(self.r,num)
            else:
                t=-heapq.heappop(self.l)
                heapq.heappush(self.l,-num)
                heapq.heappush(self.r,t)

    def findMedian(self) -> float:
        if len(self.l)==len(self.r):
            return (-self.l[0]+self.r[0])/2
        else:
            return self.r[0]