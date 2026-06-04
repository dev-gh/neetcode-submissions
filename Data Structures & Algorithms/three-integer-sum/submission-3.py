'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k] == 0, and the indices i, j and k are all distinct.

The output should not contain any duplicate triplets. You may return the output and the triplets in any order.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]

Output: [[-1,-1,2],[-1,0,1]]

Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].

Example 2:

Input: nums = [0,1,1]

Output: []

Explanation: The only possible triplet does not sum up to 0.

Example 3:

Input: nums = [0,0,0]

Output: [[0,0,0]]

Explanation: The only possible triplet sums up to 0.

Constraints:

    3 <= nums.length <= 1000
    -10^5 <= nums[i] <= 10^5

'''
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = list()

        for i in range(len(nums)):
            # print(f'{i=}, {triplets=}')
            
            if i > 0 and nums[i] == nums[i - 1]:
                # print('duplicate')
                continue

            l = i + 1
            r = len(nums) - 1
            while l < r:
                # print(f'{l=}, {r=}')
                curr = nums[i]
                left = nums[l]
                right = nums[r]
                # print(f'{curr=}, {left=}, {right=}')

                sum = curr + left + right
                if sum == 0:
                    triplets.append([curr, left, right])
                    l += 1
                    r -= 1

                    # do not put after while - need only after checking the sum
                    # do not use if's
                    # do not use continue
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                        
                elif sum > 0:
                    r -= 1
                else:
                    l += 1
            
        return triplets


                    

            


