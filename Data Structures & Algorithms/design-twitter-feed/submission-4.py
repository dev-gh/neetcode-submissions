'''
Implement a simplified version of Twitter which allows users to post tweets, follow/unfollow each other, and view the 10 most recent tweets within their own news feed.

Users and tweets are uniquely identified by their IDs (integers).

Implement the following methods:

    Twitter() Initializes the twitter object.
    void postTweet(int userId, int tweetId) Publish a new tweet with ID tweetId by the user userId. You may assume that each tweetId is unique.
    List<Integer> getNewsFeed(int userId) Fetches at most the 10 most recent tweet IDs in the user's news feed. Each item must be posted by users who the user is following or by the user themself. Tweets IDs should be ordered from most recent to least recent.
    void follow(int followerId, int followeeId) The user with ID followerId follows the user with ID followeeId.
    void unfollow(int followerId, int followeeId) The user with ID followerId unfollows the user with ID followeeId.

Example 1:

Input:
["Twitter", "postTweet", [1, 10], "postTweet", [2, 20], "getNewsFeed", [1], "getNewsFeed", [2], "follow", [1, 2], "getNewsFeed", [1], "getNewsFeed", [2], "unfollow", [1, 2], "getNewsFeed", [1]]

Output:
[null, null, null, [10], [20], null, [20, 10], [20], null, [10]]

Explanation:
Twitter twitter = new Twitter();
twitter.postTweet(1, 10); // User 1 posts a new tweet with id = 10.
twitter.postTweet(2, 20); // User 2 posts a new tweet with id = 20.
twitter.getNewsFeed(1);   // User 1's news feed should only contain their own tweets -> [10].
twitter.getNewsFeed(2);   // User 2's news feed should only contain their own tweets -> [20].
twitter.follow(1, 2);     // User 1 follows user 2.
twitter.getNewsFeed(1);   // User 1's news feed should contain both tweets from user 1 and user 2 -> [20, 10].
twitter.getNewsFeed(2);   // User 2's news feed should still only contain their own tweets -> [20].
twitter.unfollow(1, 2);   // User 1 unfollows user 2.
twitter.getNewsFeed(1);   // User 1's news feed should only contain their own tweets -> [10].

Constraints:

    1 <= userId, followerId, followeeId <= 500
    0 <= tweetId <= 10^4
    All the tweets have unique IDs.
    At most 3 * 10^4 calls will be made to postTweet, getNewsFeed, follow, and unfollow.
    A user cannot follow themself.



Topics


Recommended Time & Space Complexity

You should aim for a solution with O(nlogn) time for each getNewsFeed() function call, O(1) time for the remaining methods, and O((N * m) + (N * M) + n) space, where n is the number of followeeIds associated with the userId, m is the maximum number of tweets by any user, N is the total number of userIds, and M is the maximum number of followees for any user.
'''
class Twitter:

    def __init__(self):
        self.followers = defaultdict(set)
        self.messages = defaultdict(list)
        self.counter = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.messages[userId].append((self.counter, tweetId))
        self.counter -= 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        result = []
        recent = []

        for id in self.followers[userId]:
            if len(self.messages[id]) >= 1:
                msg_counter, msg = self.messages[id][-1]
                heapq.heappush(recent, (msg_counter, msg, id, -1))
        
        if len(self.messages[userId]) >= 1:
            msg_counter, msg = self.messages[userId][-1]
            heapq.heappush(recent, (msg_counter, msg, userId, -1))
        
        while recent:
            msg_counter, msg, uid, idx = heapq.heappop(recent)
            result.append(msg)

            if len(result) == 10:
                return result
            else:
                next_idx = idx - 1
                if len(self.messages[uid]) >= -next_idx:
                    uid_msg_counter, uid_msg = self.messages[uid][next_idx]

                    heapq.heappush(recent, (uid_msg_counter, uid_msg, uid, next_idx))

        return result


    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].discard(followeeId)
        
