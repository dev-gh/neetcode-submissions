'''
Given a string s, return the number of substrings within s that are palindromes.

A palindrome is a string that reads the same forward and backward.

Example 1:

Input: s = "abc"

Output: 3

Explanation: "a", "b", "c".

Example 2:

Input: s = "aaa"

Output: 6

Explanation: "a", "a", "a", "aa", "aa", "aaa". Note that different substrings are counted as different palindromes even if the string contents are the same.

Constraints:

    1 <= s.length <= 1000
    s consists of lowercase English letters.

'''
class Solution:
    def countSubstrings(self, s: str) -> int:
        counter = 0

        for i in range(len(s)):
            left = right = i

            while left >= 0 and right < len(s):
                if s[left] == s[right]:
                    counter += 1
                    left -= 1
                    right += 1
                else:
                    break

            left = i
            right = i + 1
            
            while left >= 0 and right < len(s):
                if s[left] == s[right]:
                    counter += 1
                    left -= 1
                    right += 1
                else:
                    break

        return counter

        