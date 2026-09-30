'''
You are given an array nums of integers, which may contain duplicates. Return all possible subsets.

The solution must not contain duplicate subsets. You may return the solution in any order.

Example 1:

Input: nums = [1,2,1]

Output: [[],[1],[1,2],[1,1],[1,2,1],[2]]

Example 2:

Input: nums = [7,7]

Output: [[],[7], [7,7]]

Constraints:

    1 <= nums.length <= 11
    -20 <= nums[i] <= 20



Topics


Recommended Time & Space Complexity

You should aim for a solution as good or better than O(n * (2^n)) time and O(n) space, where n is the size of the input array.

'''
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        stack = [([], nums)]

        while stack:
            choosen, left = stack.pop()
            #print(f'{choosen=}, {left=}')
            result.append(choosen)

            for i in range(len(left)):
                if i > 0 and left[i] == left[i - 1]:
                    continue
                char = left[i]
                new_left = left[i + 1:]
                stack.append((choosen + [char], new_left))
                #print(f'apd: {stack[-1]=}')
        
        return result


        