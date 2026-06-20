class Twitter:

    def __init__(self):
        self.d={}
        self.f={}
        self.time=0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.d:
            self.d[userId]=[]
        self.d[userId].append([self.time,tweetId])
        self.time-=1

    def getNewsFeed(self, userId: int) -> List[int]:
        res=[]
        minheap=[]

        if userId not in self.f:
            self.f[userId]=set()
        self.f[userId].add(userId)

        for i in self.f[userId]:
            if i in self.d:
                index= len(self.d[i])-1
                tim,twt=self.d[i][index]
                minheap.append([tim,twt,i,index-1])
        heapq.heapify(minheap)
        while minheap and len(res)<10:
            tim,twt,i,index=heapq.heappop(minheap)
            res.append(twt)
            if index>=0:
                tim,twt=self.d[i][index]
                heapq.heappush(minheap,[tim,twt,i,index-1])
        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.f:
            self.f[followerId]=set()
        self.f[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.f:
            if followeeId in self.f[followerId]:
                self.f[followerId].remove(followeeId)
