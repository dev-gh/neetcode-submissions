'''
You are given two strings s1 and s2.

Return true if s2 contains a permutation of s1, or false otherwise. That means if a permutation of s1 exists as a substring of s2, then return true.

Both strings only contain lowercase letters.

Example 1:

Input: s1 = "abc", s2 = "lecabee"

Output: true

Explanation: The substring "cab" is a permutation of "abc" and is present in "lecabee".

Example 2:

Input: s1 = "abc", s2 = "lecaabee"

Output: false

Constraints:

    1 <= s1.length, s2.length <= 1000

'''
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        frequencies_s1 = defaultdict(int)
        frequencies_window = defaultdict(int)

        for c in s1:
            frequencies_s1[c] += 1

        # print(f'{frequencies_s1=}')
        left = 0
        for right in range(len(s2)):
            frequencies_window[s2[right]] += 1
            # window_length = sum(frequencies_window.values())
            window_length = right - left + 1

            if window_length > len(s1):
                if frequencies_window[s2[left]] > 1:
                    frequencies_window[s2[left]] -= 1
                else:
                    frequencies_window.pop(s2[left])
                
                left += 1
                
            # print(f'{frequencies_window=}')
            if frequencies_s1 == frequencies_window:
                return True
        
        return False