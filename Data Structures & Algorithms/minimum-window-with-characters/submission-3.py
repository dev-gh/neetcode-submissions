'''
Given two strings s and t, return the shortest substring of s such that every character in t, including duplicates, is present in the substring. If such a substring does not exist, return an empty string "".

You may assume that the correct output is always unique.

Example 1:

Input: s = "OUZODYXAZV", t = "XYZ"

Output: "YXAZ"

Explanation: "YXAZ" is the shortest substring that includes "X", "Y", and "Z" from string t.

Example 2:

Input: s = "xyz", t = "xyz"

Output: "xyz"

Example 3:

Input: s = "x", t = "xy"

Output: ""

Constraints:

    1 <= s.length <= 1000
    1 <= t.length <= 1000
    s and t consist of uppercase and lowercase English letters.

'''
# NEEDS WORK
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freq_t = defaultdict(int)
        freq_window = defaultdict(int)

        left = 0
        strings = list()

        for c in t:
            freq_t[c] += 1

        for right in range(len(s)):
            freq_window[s[right]] += 1

            skip = False
            for char, freq in freq_t.items():
                if char not in freq_window or freq_window[char] < freq:
                    skip = True
                    break
                
            if skip:
                continue

            sstring = s[left:right + 1]
            print(f'set {sstring=}')


            shrinking = True
            while left < right and shrinking:
                freq_window[s[left]] -= 1
                left += 1
                for char, freq in freq_t.items():
                    if char not in freq_window or freq_window[char] < freq:
                        shrinking = False

                if shrinking:
                    sstring = s[left:right + 1]
                    print(f'updated {sstring=}')
            
            strings.append(sstring)
            print(f'appended {strings=}')
        
        if len(strings) > 0:
            min_sstring = strings[0]
            for s in strings:
                if len(s) < len(min_sstring):
                    min_sstring = s

            return min_sstring
        else:
            return ""
        