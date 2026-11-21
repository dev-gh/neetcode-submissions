'''
You are given an array of positive integers nums.

Return true if you can partition the array into two subsets, subset1 and subset2 where sum(subset1) == sum(subset2). Otherwise, return false.

Example 1:

Input: nums = [1,2,3,4]

Output: true

Explanation: The array can be partitioned as [1, 4] and [2, 3].

Example 2:

Input: nums = [1,2,3,4,5]

Output: false

Constraints:

    1 <= nums.length <= 100
    1 <= nums[i] <= 50

'''
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        half = total // 2
        rem = total % 2

        if  rem != 0:
            return False

        achievable = set()
        achievable.add(0)

        for n in nums:
            tmp = set()
            for a in achievable:
                s = n + a

                if s not in achievable:
                    tmp.add(s)
               
            achievable.update(tmp)
 
            if half in tmp:
                return True
             
                
        return False