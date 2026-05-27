'''
Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:

Input: strs = ["act","pots","tops","cat","stop","hat"]

Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]

Example 2:

Input: strs = ["x"]

Output: [["x"]]

Example 3:

Input: strs = [""]

Output: [[""]]

Constraints:

    1 <= strs.length <= 1000.
    0 <= strs[i].length <= 100
    strs[i] is made up of lowercase English letters.

'''
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        known = dict()
        
        def get_count(string: str):
            counter = [0] * 26 # english alphabet number
            for s in string:
                index = ord(s) - ord('a')
                if counter[index] == 0:
                    counter[index] = 1
                else:
                    counter[index] += 1

            return tuple(counter)

        for single_str in strs:
            key = get_count(single_str)
            if known.get(key) == None:
                known[key] = [ single_str ]
            else:
                known[key].append(single_str)
            
        return [v for v in known.values()]

        
        
        



        