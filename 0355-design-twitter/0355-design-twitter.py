class Twitter:

    def __init__(self):
        self.count = 0
        self.user_posts = defaultdict(list) # [(count, tweet)]
        self.follows = defaultdict(set)
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.user_posts[userId].append([self.count,tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []
        # Adding user himself in his following list
        self.follows[userId].add(userId)

        for followeeId in self.follows[userId]:
            # check the followee has made post
            if followeeId in self.user_posts:
                index = len(self.user_posts[followeeId]) - 1
                count, tweetId = self.user_posts[followeeId][index]
                heapq.heappush(minHeap,([count, tweetId, followeeId, index-1]))

        while minHeap and len(res) < 10:
            count, tweetId , followeeId, index = heappop(minHeap)
            res.append(tweetId)
            if index >=0:
                count, tweetId = self.user_posts[followeeId][index]
                heapq.heappush(minHeap,([count, tweetId, followeeId, index-1]))
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)