'''
Valid Parentheses
Easy Topics Company Tags
Hints

You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.

The input string s is valid if and only if:

    Every open bracket is closed by the same type of close bracket.
    Open brackets are closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.

Return true if s is a valid string, and false otherwise.

Example 1:

Input: s = "[]"

Output: true

Example 2:

Input: s = "([{}])"

Output: true

Example 3:

Input: s = "[(])"

Output: false

Explanation: The brackets are not closed in the correct order.

Constraints:

    1 <= s.length <= 1000

'''
class Solution:
    def isValid(self, s: str) -> bool:
        brackets = list()

        for i in range(len(s)):
            if s[i] == '[' or s[i] == '{' or s[i] == '(':
                brackets.append(s[i])
                continue

            if len(brackets) == 0:
                return False
            
            if s[i] == ']' and '[' != brackets.pop():
                return False
       
            if s[i] == '}' and '{' != brackets.pop():
                return False

            if s[i] == ')' and '(' != brackets.pop():
                return False

        return len(brackets) == 0