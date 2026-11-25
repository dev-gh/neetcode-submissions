'''
Given an array of meeting time interval objects consisting of start and end times [[start_1,end_1],[start_2,end_2],...] (start_i < end_i), find the minimum number of rooms required to schedule all meetings without any conflicts.

Note: (0,8),(8,10) is NOT considered a conflict at 8.

Example 1:

Input: intervals = [(0,40),(5,10),(15,20)]

Output: 2

Explanation:
room1: (0,40)
room2: (5,10),(15,20)

Example 2:

Input: intervals = [(4,9)]

Output: 1

Constraints:

    0 <= intervals.length <= 100,000
    0 <= intervals[i].start < intervals[i].end <= 1,000,000

'''
"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) == 0:
            return 0

        intervals.sort(key=lambda x: x.start)

        rooms = [intervals[0].end]
        heapq.heapify(rooms)

        for i in range(1, len(intervals)):
            closest = heapq.heappop(rooms)
            
            if closest > intervals[i].start:
                heapq.heappush(rooms, closest)

            heapq.heappush(rooms, intervals[i].end)
                
        return len(rooms)
            


        