"""
LeetCode 355: Design Twitter

Problem Statement:
Design a simplified version of Twitter where users can post tweets, follow/unfollow another user, 
and see the 10 most recent tweets in the user's news feed.

Implement the Twitter class:
- Twitter() Initializes your twitter object.
- void postTweet(int userId, int tweetId) Composes a new tweet with ID tweetId by the user userId.
- List<Integer> getNewsFeed(int userId) Gets the 10 most recent tweet IDs in the user's news feed.
  - Retrieves the most recent tweets posted by the user and the users they follow.
  - Tweets must be ordered from most recent to least recent.
- void follow(int followerId: int, followeeId: int) The user with ID followerId starts following the user with ID followeeId.
- void unfollow(int followerId: int, followeeId: int) The user with ID followerId stops following the user with ID followeeId.

Example:
Input:
["Twitter", "postTweet", "getNewsFeed", "follow", "postTweet", "getNewsFeed", "unfollow", "getNewsFeed"]
[[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]]
Output:
[null, null, [5], null, null, [6, 5], null, [5]]

Logic:
1. Use defaultdict to maintain user's followers and tweets
2. For each tweet, store both tweetId and timestamp
3. For getNewsFeed:
   - Use heap to merge tweets from user and followees
   - Maintain only top 10 most recent tweets
4. Time Complexity:
   - postTweet: O(1)
   - getNewsFeed: O(N log N) where N is total tweets from user and followees
   - follow/unfollow: O(1)
5. Space Complexity: O(U + T) where U is number of users and T is total tweets
"""

from collections import defaultdict
import heapq
from typing import List


class Twitter:
    def __init__(self):
        """Initialize your data structure here."""
        self.tweets = defaultdict(list)  # userId -> [(timestamp, tweetId)]
        self.follows = defaultdict(set)  # userId -> set of followeeIds
        self.time = 0  # Global timestamp for ordering tweets

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        Time complexity: O(1)
        """
        self.time += 1
        self.tweets[userId].append((-self.time, tweetId))  # Negative time for max heap

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed.
        Each item in the news feed must be posted by users who the user followed or by the user themself.
        Tweets must be ordered from most recent to least recent.
        Time complexity: O(N log N) where N is total number of tweets from user and followees
        """
        # Get all users we need tweets from (user + followees)
        users = self.follows[userId] | {userId}
        
        # Get the most recent tweets using a heap
        heap = []
        for user in users:
            for time, tweetId in self.tweets[user][-10:]:  # Only consider last 10 tweets
                heapq.heappush(heap, (time, tweetId))
                if len(heap) > 10:
                    heapq.heappop(heap)
        
        # Return tweets in reverse chronological order
        return [tweetId for _, tweetId in sorted(heap)]

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee.
        Time complexity: O(1)
        """
        if followerId != followeeId:  # Can't follow yourself
            self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee.
        Time complexity: O(1)
        """
        self.follows[followerId].discard(followeeId)


def run_test_cases():
    # Test case 1: Example from problem statement
    print("Test case 1: Basic functionality")
    twitter = Twitter()
    
    print("1. Post tweet: User 1 posts tweet 5")
    twitter.postTweet(1, 5)
    
    print("2. Get news feed for User 1")
    result1 = twitter.getNewsFeed(1)
    print(f"Expected: [5]")
    print(f"Got: {result1}")
    print(f"Pass? {result1 == [5]}\n")
    
    print("3. User 1 follows User 2")
    twitter.follow(1, 2)
    
    print("4. User 2 posts tweet 6")
    twitter.postTweet(2, 6)
    
    print("5. Get news feed for User 1")
    result2 = twitter.getNewsFeed(1)
    print(f"Expected: [6, 5]")
    print(f"Got: {result2}")
    print(f"Pass? {result2 == [6, 5]}\n")
    
    print("6. User 1 unfollows User 2")
    twitter.unfollow(1, 2)
    
    print("7. Get news feed for User 1")
    result3 = twitter.getNewsFeed(1)
    print(f"Expected: [5]")
    print(f"Got: {result3}")
    print(f"Pass? {result3 == [5]}\n")

    # Test case 2: Multiple tweets and follows
    print("\nTest case 2: Multiple tweets and follows")
    twitter2 = Twitter()
    
    # User 1 posts multiple tweets
    twitter2.postTweet(1, 1)
    twitter2.postTweet(1, 2)
    twitter2.postTweet(1, 3)
    
    # User 2 posts tweets
    twitter2.postTweet(2, 4)
    twitter2.postTweet(2, 5)
    
    # User 1 follows User 2
    twitter2.follow(1, 2)
    
    result4 = twitter2.getNewsFeed(1)
    print("News feed after multiple tweets and follow:")
    print(f"Expected: [5, 4, 3, 2, 1]")
    print(f"Got: {result4}")
    print(f"Pass? {result4 == [5, 4, 3, 2, 1]}\n")

    # Test case 3: More than 10 tweets
    print("\nTest case 3: More than 10 tweets")
    twitter3 = Twitter()
    
    # Post 15 tweets
    for i in range(15):
        twitter3.postTweet(1, i)
    
    result5 = twitter3.getNewsFeed(1)
    print("News feed should show only 10 most recent tweets:")
    print(f"Expected: [14, 13, 12, 11, 10, 9, 8, 7, 6, 5]")
    print(f"Got: {result5}")
    print(f"Pass? {result5 == [14, 13, 12, 11, 10, 9, 8, 7, 6, 5]}\n")

    # Test case 4: Unfollow non-existent user
    print("\nTest case 4: Edge cases")
    twitter4 = Twitter()
    twitter4.unfollow(1, 2)  # Should not raise error
    result6 = twitter4.getNewsFeed(1)
    print("News feed for user with no tweets:")
    print(f"Expected: []")
    print(f"Got: {result6}")
    print(f"Pass? {result6 == []}")


if __name__ == "__main__":
    run_test_cases()
