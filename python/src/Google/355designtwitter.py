from collections import defaultdict, deque
import heapq


class Twitter:
    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)  # user_id -> list of (time, tweet_id)
        # user_id -> set of followed user_ids
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.tweets[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> list[int]:
        # Min-heap to keep the top 10 tweets
        min_heap = []
        # Add the tweets from the user themselves
        for time, tweetId in self.tweets[userId]:
            heapq.heappush(min_heap, (time, tweetId))
            if len(min_heap) > 10:
                heapq.heappop(min_heap)
        # Add tweets from users the user follows
        for followee in self.following[userId]:
            for time, tweetId in self.tweets[followee]:
                heapq.heappush(min_heap, (time, tweetId))
                if len(min_heap) > 10:
                    heapq.heappop(min_heap)
        # Extract tweet_ids from the heap and return them in the correct order
        return [tweetId for time, tweetId in sorted(min_heap, reverse=True)]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)


# Example usage:
twitter = Twitter()
twitter.postTweet(1, 5)
twitter.follow(1, 2)
twitter.postTweet(2, 6)
print(twitter.getNewsFeed(1))  # Output: [6, 5]
twitter.unfollow(1, 2)
print(twitter.getNewsFeed(1))  # Output: [5]
