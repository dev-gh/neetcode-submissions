'''
You are given an integer array nums where nums[i] represents the amount of money the ith house has. The houses are arranged in a circle, i.e. the first house and the last house are neighbors.

You are planning to rob money from the houses, but you cannot rob two adjacent houses because the security system will automatically alert the police if two adjacent houses were both broken into.

Return the maximum amount of money you can rob without alerting the police.

Example 1:

Input: nums = [3,4,3]

Output: 4

Explanation: You cannot rob nums[0] + nums[2] = 6 because nums[0] and nums[2] are adjacent houses. The maximum you can rob is nums[1] = 4.

Example 2:

Input: nums = [2,9,8,3,6]

Output: 15

Explanation: You cannot rob nums[0] + nums[2] + nums[4] = 16 because nums[0] and nums[4] are adjacent houses. The maximum you can rob is nums[1] + nums[4] = 15.

Constraints:

    1 <= nums.length <= 100
    0 <= nums[i] <= 200

'''
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        if len(nums) == 2:
            return max(nums[0], nums[1])
            
        def check(inp: List[int]) -> int:
            if len(inp) == 1:
                return inp[0]
    
            if len(inp) == 2:
                return max(inp[0], inp[1])
            
            dp = [0] * len(inp)
    
            dp[0] = inp[0]
            dp[1] = max(inp[0], inp[1])
    
            last = len(inp)
            for n in range(2, last):
                dp[n] = max(inp[n] + dp[n - 2], dp[n - 1])
    
            return dp[-1]

        return max(check(nums[:-1]), check(nums[1:]))
            