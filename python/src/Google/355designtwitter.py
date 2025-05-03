"""
LeetCode 355 - Design Twitter

Design a simplified version of Twitter where users can post tweets, follow/unfollow another user,
and is able to see the 10 most recent tweets in the user's news feed.

Implement the Twitter class:
- Twitter() Initializes your twitter object.
- void postTweet(int userId, int tweetId) Composes a new tweet with ID tweetId by the user userId.
- List<Integer> getNewsFeed(int userId) Retrieves the 10 most recent tweet IDs in the user's news feed.
  Each item in the news feed must be posted by users who the user followed or by the user themself.
  Tweets must be ordered from most recent to least recent.
- void follow(int followerId, int followeeId) The user with ID followerId started following the user with ID followeeId.
- void unfollow(int followerId, int followeeId) The user with ID followerId started unfollowing the user with ID followeeId.

Example:
Input:
["Twitter", "postTweet", "getNewsFeed", "follow", "postTweet", "getNewsFeed", "unfollow", "getNewsFeed"]
[[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]]
Output:
[null, null, [5], null, null, [6, 5], null, [5]]
"""
from collections import defaultdict, deque
import heapq


class Twitter:
    def __init__(self):
        """Initialize Twitter with empty tweet storage and following relationships."""
        self.time = 0  # Global timestamp for ordering tweets
        self.tweets = defaultdict(list)  # user_id -> list of (time, tweet_id)
        self.following = defaultdict(set)  # user_id -> set of followed user_ids

    def postTweet(self, userId: int, tweetId: int) -> None:
        """Post a new tweet. Time complexity: O(1)"""
        self.time += 1
        self.tweets[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> list[int]:
        """
        Get 10 most recent tweets from user's feed.
        Time complexity: O(N log k) where N is total tweets and k is 10
        """
        min_heap = []  # Min-heap to keep the top 10 tweets
        
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
                    
        # Return tweets in reverse chronological order
        return [tweetId for time, tweetId in sorted(min_heap, reverse=True)]

    def follow(self, followerId: int, followeeId: int) -> None:
        """Follow a user. Time complexity: O(1)"""
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """Unfollow a user. Time complexity: O(1)"""
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)


def test_twitter():
    """Test driver for Twitter implementation"""
    # Test case 1: Basic functionality
    print("Test case 1: Basic functionality")
    twitter = Twitter()
    twitter.postTweet(1, 5)
    assert twitter.getNewsFeed(1) == [5], "Basic tweet test failed"
    print("Basic tweet test passed")

    # Test case 2: Follow and unfollow
    print("\nTest case 2: Follow and unfollow functionality")
    twitter.follow(1, 2)
    twitter.postTweet(2, 6)
    assert twitter.getNewsFeed(1) == [6, 5], "Follow test failed"
    print("Follow test passed")
    
    twitter.unfollow(1, 2)
    assert twitter.getNewsFeed(1) == [5], "Unfollow test failed"
    print("Unfollow test passed")

    # Test case 3: News feed ordering
    print("\nTest case 3: News feed ordering")
    twitter2 = Twitter()
    twitter2.postTweet(1, 1)
    twitter2.postTweet(1, 2)
    twitter2.postTweet(1, 3)
    twitter2.postTweet(1, 4)
    twitter2.postTweet(1, 5)
    assert twitter2.getNewsFeed(1) == [5,4,3,2,1], "News feed ordering test failed"
    print("News feed ordering test passed")

    # Test case 4: Multiple users
    print("\nTest case 4: Multiple users interaction")
    twitter3 = Twitter()
    twitter3.postTweet(1, 10)
    twitter3.postTweet(2, 20)
    twitter3.postTweet(3, 30)
    twitter3.follow(1, 2)
    twitter3.follow(1, 3)
    feed = twitter3.getNewsFeed(1)
    assert feed == [30,20,10], f"Multiple users test failed. Got {feed}"
    print("Multiple users test passed")

    print("\nAll test cases passed!")


if __name__ == "__main__":
    test_twitter()
