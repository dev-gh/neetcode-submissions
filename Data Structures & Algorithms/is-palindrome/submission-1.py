'''
Given a string s, return true if it is a palindrome, otherwise return false.

A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.

Note: Alphanumeric characters consist of letters (A-Z, a-z) and numbers (0-9).

Example 1:

Input: s = "Was it a car or a cat I saw?"

Output: true

Explanation: After considering only alphanumerical characters we have "wasitacaroracatisaw", which is a palindrome.

Example 2:

Input: s = "tab a cat"

Output: false

Explanation: "tabacat" is not a palindrome.

Constraints:

    1 <= s.length <= 1000
    s is made up of only printable ASCII characters.

'''
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) <= 1:
            return True

        left_idx = 0
        right_idx = len(s) - 1
        while left_idx <= right_idx:
            print(f'{left_idx=}, {right_idx=}')
            if s[left_idx].islower() or s[left_idx].isupper() or s[left_idx].isdigit():
                if s[right_idx].islower() or s[right_idx].isupper() or s[right_idx].isdigit():
                    print(f'{s[right_idx]=}, {s[left_idx]=}')
                    if s[right_idx].lower() != s[left_idx].lower():
                        return False
                    else:
                        right_idx -= 1
                        left_idx += 1
                else:
                    right_idx -= 1
            else:
                left_idx += 1

        return True
                    
                    

