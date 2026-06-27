'''
You are given an array of integers heights where heights[i] represents the height of a bar. The width of each bar is 1.

Return the area of the largest rectangle that can be formed among the bars.

Note: This chart is known as a histogram.

Example 1:

Input: heights = [7,1,7,2,2,4]

Output: 8

Example 2:

Input: heights = [1,3,7]

Output: 7

Constraints:

    1 <= heights.length <= 1000.
    0 <= heights[i] <= 1000

'''
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        increasing_bars = [0]
        max_area = heights[0]
        for i in range(1, len(heights), 1):
            # print(f'{i=}')
            # if current is lower then last in increasing_bars - start calculating collected
            while len(increasing_bars) > 0 and heights[increasing_bars[-1]] > heights[i]:
                right = i
                j = increasing_bars.pop()
                left = increasing_bars[-1] if len(increasing_bars) > 0 else -1
                max_area = max(max_area, (right - left - 1) * heights[j])
                
                # print(f'{j=}, {i=}, {heights[j]=}, {max_area=}')

            increasing_bars.append(i)
            # print(f'{increasing_bars=}')


        # calculating max from increasing_bars
        right = increasing_bars[-1] + 1
        while len(increasing_bars) > 0:
            j = increasing_bars.pop()
            left = increasing_bars[-1] if len(increasing_bars) > 0 else -1
            area = (right - left - 1) * heights[j]
            max_area = max(max_area, area)
            # print(f'remaining {j=}, {heights[j]=}, {area=}, {max_area=}')

        return max_area
        

