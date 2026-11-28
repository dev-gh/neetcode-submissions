'''
You are given an integer array digits, where each digits[i] is the ith digit of a large integer. It is ordered from most significant to least significant digit, and it will not contain any leading zero.

Return the digits of the given integer after incrementing it by one.

Example 1:

Input: digits = [1,2,3,4]

Output: [1,2,3,5]

Explanation 1234 + 1 = 1235.

Example 2:

Input: digits = [9,9,9]

Output: [1,0,0,0]

Constraints:

    1 <= digits.length <= 100
    0 <= digits[i] <= 9

'''
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        rem = 1
        i = len(digits) - 1
        while i >= 0:
            if rem != 0:
                digits[i] += rem

            if digits[i] > 9:
                rem = 1
                digits[i] -= 10
            else:
                rem = 0
                break
            
            i -= 1

        if rem != 0:
            return [rem] + digits

        return digits



        