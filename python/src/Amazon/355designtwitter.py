import heapq
from collections import defaultdict


class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int):
        heap = []
        self.following[userId].add(userId)
        for followeeId in self.following[userId]:
            for time, tweet in self.tweets[followeeId][-10:]:
                heapq.heappush(heap, (-time, tweet))

        return [heapq.heappop(heap)[1] for _ in range(min(10, len(heap)))]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
