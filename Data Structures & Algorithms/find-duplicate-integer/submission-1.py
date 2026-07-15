'''
You are given an array of integers nums containing n + 1 integers. Each integer in nums is in the range [1, n] inclusive.

There is exactly one repeated integer in nums, and every other integer appears at most once.

Return the repeated integer.

Example 1:

Input: nums = [1,2,3,2,2]

Output: 2

Example 2:

Input: nums = [1,2,3,4,4]

Output: 4

Follow-up: Can you solve the problem without modifying the array nums and using O(1)O(1) extra space?

Constraints:

    1 <= n <= 10,000
    nums.length == n + 1
    1 <= nums[i] <= n

'''
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0
        fast = 0

        counter = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            counter += 1
            if slow == fast:
                break

        print(f'exit loop: {counter=}, {slow=}, {fast=}')
            
        slow = 0
        while True:
            slow = nums[slow]
            fast = nums[fast]

            if slow == fast:
                return slow
