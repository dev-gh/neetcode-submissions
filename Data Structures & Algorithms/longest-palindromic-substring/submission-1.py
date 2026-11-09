'''
Given a string s, return the longest substring of s that is a palindrome.

A palindrome is a string that reads the same forward and backward.

If there are multiple palindromic substrings that have the same length, return any one of them.

Example 1:

Input: s = "ababd"

Output: "bab"

Explanation: Both "aba" and "bab" are valid answers.

Example 2:

Input: s = "abbc"

Output: "bb"

Constraints:

    1 <= s.length <= 1000
    s contains only digits and English letters.

'''
class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_palindrome = ""

        for i in range(len(s)):

            left = right = i
            while left >= 0 and right < len(s):
                if s[left] == s[right]:
                    if len(max_palindrome) < right - left + 1:
                        max_palindrome = s[left:right + 1]

                    left -= 1
                    right += 1
                else:
                    break

            left = i
            right = i + 1
            while left >= 0 and right < len(s):
                if s[left] == s[right]:
                    if len(max_palindrome) < right - left + 1:
                        max_palindrome = s[left:right + 1]

                    left -= 1
                    right += 1
                else:
                    break
        
        
        return max_palindrome
             
    
