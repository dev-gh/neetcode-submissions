'''
Given an array nums of unique integers, return all possible subsets of nums.

The solution set must not contain duplicate subsets. You may return the solution in any order.

Example 1:

Input: nums = [1,2,3]

Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:

Input: nums = [7]

Output: [[],[7]]

Constraints:

    1 <= nums.length <= 10
    -10 <= nums[i] <= 10



Topics


Recommended Time & Space Complexity

You should aim for a solution with O(n * (2^n)) time and O(n) space, where n is the size of the input array.

'''
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]

        for n in nums:
            intermediate = []
            for r in result:
                intermediate.append(r + [n])

            result += intermediate

        return result

        