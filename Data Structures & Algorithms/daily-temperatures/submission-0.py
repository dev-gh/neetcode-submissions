'''
You are given an array of integers temperatures where temperatures[i] represents the daily temperatures on the ith day.

Return an array result where result[i] is the number of days after the ith day before a warmer temperature appears on a future day. If there is no day in the future where a warmer temperature will appear for the ith day, set result[i] to 0 instead.

Example 1:

Input: temperatures = [30,38,30,36,35,40,28]

Output: [1,4,1,2,1,0,0]

Example 2:

Input: temperatures = [22,21,20]

Output: [0,0,0]

Constraints:

    1 <= temperatures.length <= 1000.
    1 <= temperatures[i] <= 100

'''
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        idx_stack = [] 
        output = [0] * len(temperatures)
        
        for i in range(len(temperatures) - 1, -1, -1):
            # print(f'{i=}')
            while len(idx_stack) > 0:
                if temperatures[idx_stack[-1]] <= temperatures[i]:
                    # print(f'{temperatures[idx_stack[-1]]=} <= {temperatures[i]}')
                    idx_stack.pop()
                else:
                    output[i] = idx_stack[-1] - i
                    # print(f'{temperatures[idx_stack[-1]]=} > {temperatures[i]}')
                    idx_stack.append(i)
                    break

            if len(idx_stack) == 0:
                output[i] = 0
                # print(f'{output[i]=}')
                idx_stack.append(i)
        

        return output
            
