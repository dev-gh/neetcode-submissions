'''
Given an integer array nums and an integer k, return the k most frequent elements within the array.

The test cases are generated such that the answer is always unique.

You may return the output in any order.

Example 1:

Input: nums = [1,2,2,3,3,3], k = 2

Output: [2,3]

Example 2:

Input: nums = [7,7], k = 1

Output: [7]

Constraints:

    1 <= nums.length <= 10^4.
    -1000 <= nums[i] <= 1000
    1 <= k <= number of distinct elements in nums.

'''
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        number_occurence = dict()

        # O(n)
        for n in nums:
            if number_occurence.get(n) == None:
                number_occurence[n] = 1
            else:
                number_occurence[n] += 1
            
        #print(f'{number_occurence=}')
        
        sorted_dict = dict(sorted(number_occurence.items(), key=lambda item: item[1], reverse=True))

        #print(f'{sorted_dict=}')

        return [x for x in list(sorted_dict.keys())[:k]]



        