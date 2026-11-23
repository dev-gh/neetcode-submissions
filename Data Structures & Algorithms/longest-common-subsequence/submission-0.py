'''
Given two strings text1 and text2, return the length of the longest common subsequence between the two strings if one exists, otherwise return 0.

A subsequence is a sequence that can be derived from the given sequence by deleting some or no elements without changing the relative order of the remaining characters.

    For example, "cat" is a subsequence of "crabt".

A common subsequence of two strings is a subsequence that exists in both strings.

Example 1:

Input: text1 = "cat", text2 = "crabt" 

Output: 3 

Explanation: The longest common subsequence is "cat" which has a length of 3.

Example 2:

Input: text1 = "abcd", text2 = "abcd"

Output: 4

Example 3:

Input: text1 = "abcd", text2 = "efgh"

Output: 0

Constraints:

    1 <= text1.length, text2.length <= 1000
    text1 and text2 consist of only lowercase English characters.

'''
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        rows, cols = len(text1) + 1, len(text2) + 1
        dp = [[0 for _ in range(cols)] for _ in range(rows)]

        dp[0][0] = 0

        for i in range(1, rows):
            for j in range(1, cols):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        

        return dp[-1][-1]

