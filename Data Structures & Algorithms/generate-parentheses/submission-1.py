'''
You are given an integer n. Return all well-formed parentheses strings that you can generate with n pairs of parentheses.

Example 1:

Input: n = 1

Output: ["()"]

Example 2:

Input: n = 3

Output: ["((()))","(()())","(())()","()(())","()()()"]

You may return the answer in any order.

Constraints:

    1 <= n <= 7



Topics


Recommended Time & Space Complexity

You should aim for a solution as good or better than O(4^n / sqrt(n)) time and O(n) space, where n is the number of parenthesis pairs in the string.

'''
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        stack = [("", 0, 0)]

        while stack:
            current, opened, closed = stack.pop()
            
            if len(current) == n * 2:
                result.append(current)
                continue
            
            if opened < n:
                stack.append((current + '(', opened + 1, closed))
            if closed < opened:
                stack.append((current + ')', opened, closed + 1))


        return result 