'''
Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].

Each product is guaranteed to fit in a 32-bit integer.

Follow-up: Could you solve it in O(n)O(n) time without using the division operation?

Example 1:

Input: nums = [1,2,4,6]

Output: [48,24,12,8]

Example 2:

Input: nums = [-1,0,1,2,3]

Output: [0,-6,0,0,0]

Constraints:

    2 <= nums.length <= 1000
    -20 <= nums[i] <= 20

'''
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # space O(n)
        products = [1] * len(nums)

        # # time O(n)
        # for j in range(len(products)):
        #     # time O(n)
        #     for i in range(len(nums)):
        #         if i == j:
        #             continue
        #         products[j] = products[j] * nums[i]

        products_left = [1] * len(nums)
        for i in range(len(nums)):
            if i == 0:
                products_left[i] = nums[i]
            else:
                products_left[i] = products_left[i - 1] * nums[i]

        products_right = [1] * len(nums)
        for j in range(len(nums) - 1, -1, -1):
            if j == len(nums) - 1:
                products_right[j] = nums[j]
            else:
                products_right[j] = products_right[j + 1] * nums[j]

        for k in range(len(nums)):
            if k == 0:
                products[k] = products_right[k + 1]
            elif k == len(nums) - 1:
                products[k] = products_left[k - 1]
            else:
                products[k] = products_left[k - 1] * products_right[k + 1]
            
        print(f'{products_left=}, {products_right=}, {products=}')
        
        return products
        