'''
Given a string s, find the length of the longest substring without duplicate characters.

A substring is a contiguous sequence of characters within a string.

Example 1:

Input: s = "zxyzxyz"

Output: 3

Explanation: The string "xyz" is the longest without duplicate characters.

Example 2:

Input: s = "xxxx"

Output: 1

Constraints:

    0 <= s.length <= 1000
    s may consist of printable ASCII characters.

'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        positions = dict()
        max_length = 0
        while right < len(s):
            char = s[right]
            if char in positions:
                left = max(left, positions[char] + 1)

            max_length = max(max_length, right - left + 1)
            positions[char] = right
            right += 1
        
        return max_length

            