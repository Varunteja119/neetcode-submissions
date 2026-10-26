class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> list[int]:
        users = self.following[userId] | {userId}
        heap = []
        for user in users:
            for time, tweetId in self.tweets[user][-10:]:
                heapq.heappush(heap, (-time, tweetId))
        feed = []
        while heap and len(feed) < 10:
            neg_time, tweetId = heapq.heappop(heap)
            feed.append(tweetId)
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)