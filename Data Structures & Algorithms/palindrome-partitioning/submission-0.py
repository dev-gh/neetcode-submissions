'''
Given a string s, split s into substrings where every substring is a palindrome. Return all possible lists of palindromic substrings.

You may return the solution in any order.

Example 1:

Input: s = "aab"

Output: [["a","a","b"],["aa","b"]]

Example 2:

Input: s = "a"

Output: [["a"]]

Constraints:

    1 <= s.length <= 20
    s contains only lowercase English letters.



Topics


Recommended Time & Space Complexity

You should aim for a solution with O(n * (2^n)) time and O(n) space, where n is the length of the input string.

'''
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        stack = [([], s)]

        def isPalindrome(input: str) -> bool:
            left = 0
            right = len(input) - 1

            while left < right:
                if input[left] != input[right]:
                    return False
                
                left += 1
                right -= 1
            
            return True

                
        
        while stack:
            pals, left = stack.pop()

            if len(left) == 0 and len(pals) != 0:
                result.append(pals)
                continue

            for i in range(1, len(left) + 1):
                check = left[:i]
                if isPalindrome(check):
                    stack.append((pals + [check], left[i:]))

        
        return result