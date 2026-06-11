class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        f=[]
        for i in points:
            if len(f)<k:
                heapq.heappush(f,[-math.sqrt(i[0]**2+i[1]**2),i])
            else:
                heapq.heappushpop(f,[-math.sqrt(i[0]**2+i[1]**2),i])
        return [l[1] for l in f]