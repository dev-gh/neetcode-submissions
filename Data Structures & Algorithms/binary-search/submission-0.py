'''
You are given an array of distinct integers nums, sorted in ascending order, and an integer target.

Implement a function to search for target within nums. If it exists, then return its index, otherwise, return -1.

Your solution must run in O(logn)O(logn) time.

Example 1:

Input: nums = [-1,0,2,4,6,8], target = 4

Output: 3

Example 2:

Input: nums = [-1,0,2,4,6,8], target = 3

Output: -1

Constraints:

    1 <= nums.length <= 10000.
    -10000 < nums[i], target < 10000
    All the integers in nums are unique.

'''
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums) - 1

        while j >= i:
            k = i + int((j - i) / 2)

            if nums[k] > target:
                j = k - 1
            elif nums[k] < target:
                i = k + 1
            else:
                return k
            
        return -1

        # i = 0
        # j = len(nums) - 1
        # k = 0

        # while j >= i:
        #     k = i + int((j - i) / 2)

        #     if nums[k] > target:
        #         print('>')
        #         j = k if j != k else j - 1
        #     elif nums[k] < target:
        #         i = k if i != k else k + 1
        #         print('<')
        #     else:
        #         break
            
        #     print(f'{i=}, {j=}, {k=}')


        # return k if nums[k] == target else -1
