355. Design Twitter
https://leetcode.com/problems/design-twitter/description/

Design a simplified version of Twitter where users can post tweets, follow/unfollow another user, and is able to see the 10 most recent tweets in the user's news feed.

Implement the Twitter class:

Twitter() Initializes your twitter object.
void postTweet(int userId, int tweetId) Composes a new tweet with ID tweetId by the user userId. Each call to this function will be made with a unique tweetId.
List<Integer> getNewsFeed(int userId) Retrieves the 10 most recent tweet IDs in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user themself. Tweets must be ordered from most recent to least recent.
void follow(int followerId, int followeeId) The user with ID followerId started following the user with ID followeeId.
void unfollow(int followerId, int followeeId) The user with ID followerId started unfollowing the user with ID followeeId.
 

Example 1:

Input
["Twitter", "postTweet", "getNewsFeed", "follow", "postTweet", "getNewsFeed", "unfollow", "getNewsFeed"]
[[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]]
Output
[null, null, [5], null, null, [6, 5], null, [5]]

Explanation
Twitter twitter = new Twitter();
twitter.postTweet(1, 5); // User 1 posts a new tweet (id = 5).
twitter.getNewsFeed(1);  // User 1's news feed should return a list with 1 tweet id -> [5]. return [5]
twitter.follow(1, 2);    // User 1 follows user 2.
twitter.postTweet(2, 6); // User 2 posts a new tweet (id = 6).
twitter.getNewsFeed(1);  // User 1's news feed should return a list with 2 tweet ids -> [6, 5]. Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
twitter.unfollow(1, 2);  // User 1 unfollows user 2.
twitter.getNewsFeed(1);  // User 1's news feed should return a list with 1 tweet id -> [5], since user 1 is no longer following user 2.
 

Constraints:

1 <= userId, followerId, followeeId <= 500
0 <= tweetId <= 104
All the tweets have unique IDs.
At most 3 * 104 calls will be made to postTweet, getNewsFeed, follow, and unfollow.
A user cannot follow himself.



class Tweet:
    def __init__(self, tweet_id, time_stamp):
        self.tweet_id = tweet_id
        self.time = time_stamp
        self.next = None

class User:
    def __init__(self, id):
        self.id = id
        self.followed = set()
        self.followed.add(id)
        self.tweet_head = None
    
    def follow(self, id):
        self.followed.add(id)

    def unfollow(self, id):
        if id not in self.followed:
            return
        self.followed.remove(id)
    
    def post(self, tweet_id, time_stamp):
        tweet = Tweet(tweet_id, time_stamp)
        tweet.next = self.tweet_head
        self.tweet_head = tweet

class Twitter:
    def __init__(self):
        self.time_stamp = 0
        self.user_map = {} # {id : User}

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.user_map:
            self.user_map[userId] = User(userId)
        self.user_map[userId].post(tweetId, self.time_stamp)
        self.time_stamp += 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        if userId not in self.user_map:
            return res

        max_heap = []
        user_ids = self.user_map[userId].followed
        for user_id in user_ids:
            if self.user_map[user_id].tweet_head:
                heapq.heappush(max_heap, (-self.user_map[user_id].tweet_head.time, self.user_map[user_id].tweet_head))
        
        while max_heap and len(res) < 10:
            _, tweet = heapq.heappop(max_heap)
            res.append(tweet.tweet_id)

            if tweet.next:
                heapq.heappush(max_heap, (-tweet.next.time, tweet.next))
        
        return res
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.user_map:
            self.user_map[followerId] = User(followerId)
        if followeeId not in self.user_map:
            self.user_map[followeeId] = User(followeeId)
        
        self.user_map[followerId].follow(followeeId)
        return

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.user_map:
            return
        
        self.user_map[followerId].unfollow(followeeId)




# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
