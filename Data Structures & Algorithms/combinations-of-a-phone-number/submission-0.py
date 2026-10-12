'''
ou are given a string digits made up of digits from 2 through 9 inclusive.

Each digit (not including 1) is mapped to a set of characters as shown below:

A digit could represent any one of the characters it maps to.

Return all possible letter combinations that digits could represent. You may return the answer in any order.

Phone keypad letter mapping

Example 1:

Input: digits = "34"

Output: ["dg","dh","di","eg","eh","ei","fg","fh","fi"]

Example 2:

Input: digits = ""

Output: []

Constraints:

    0 <= digits.length <= 4
    2 <= digits[i] <= 9

'''
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        chars = {2: "abc", 3: "def", 4: "ghi", 5: "jkl", 6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz"}

        if len(digits) == 0:
            return []

        stack = [([], digits)]

        while stack:
            combinations, left = stack.pop()
            #print(f'{combinations=}, {left=}')

            if len(left) == 0:
                return combinations

            if len(combinations) == 0:
                first_digit = int(left[0])
                init_list = []
                str_mapped = chars[first_digit]
                #print(f'{first_digit=}, {str_mapped=}')
                for ch in str_mapped:
                    #print(f'{init_list=}')
                    init_list.append(ch)

                new_left = left[1:]
                stack.append((init_list, new_left))
                continue
            
            new_combinations = []
            next_digit = int(left[0])
            new_left = left[1:]
            for c in combinations:
                for ch in chars[next_digit]:
                    new_combinations.append(c + ch)
            
            stack.append((new_combinations, new_left))

        
        
        