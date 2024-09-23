package amazon;

import java.util.*;

public class DesignTwitter355 {
    private int time;
    private Map<Integer, Set<Integer>> following;
    private Map<Integer, List<Tweet>> tweets;

    public DesignTwitter355() {
        this.time = 0;
        this.following = new HashMap<>();
        this.tweets = new HashMap<>();
    }

    public void postTweet(int userId, int tweetId) {
        tweets.putIfAbsent(userId, new ArrayList<>());
        tweets.get(userId).add(new Tweet(time++, tweetId));
    }

    public List<Integer> getNewsFeed(int userId) {
        PriorityQueue<Tweet> heap = new PriorityQueue<>((a, b) -> b.time - a.time);
        if (following.get(userId) != null) {
            for (int followeeId : following.get(userId)) {
                if (tweets.get(followeeId) != null) {
                    for (Tweet t : tweets.get(followeeId).subList(Math.max(0, tweets.get(followeeId).size() - 10), tweets.get(followeeId).size())) {
                        heap.add(t);
                    }
                }
            }
        }
        List<Integer> res = new ArrayList<>();
        int count = 0;
        while (!heap.isEmpty() && count < 10) {
            res.add(heap.poll().tweetId);
            count++;
        }
        return res;
    }

    public void follow(int followerId, int followeeId) {
        following.putIfAbsent(followerId, new HashSet<>());
        following.get(followerId).add(followeeId);
    }

    public void unfollow(int followerId, int followeeId) {
        if (following.get(followerId) != null) {
            following.get(followerId).remove(followeeId);
        }
    }

    class Tweet {
        int time;
        int tweetId;

        public Tweet(int time, int tweetId) {
            this.time = time;
            this.tweetId = tweetId;
        }
    }
}
