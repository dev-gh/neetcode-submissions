'''
You are given an array prerequisites where prerequisites[i] = [a, b] indicates that you must take course b first if you want to take course a.

The pair [0, 1], indicates that must take course 1 before taking course 0.

There are a total of numCourses courses you are required to take, labeled from 0 to numCourses - 1.

Return true if it is possible to finish all courses, otherwise return false.

Example 1:

Input: numCourses = 2, prerequisites = [[0,1]]

Output: true

Explanation: First take course 1 (no prerequisites) and then take course 0.

Example 2:

Input: numCourses = 2, prerequisites = [[0,1],[1,0]]

Output: false

Explanation: In order to take course 1 you must take course 0, and to take course 0 you must take course 1. So it is impossible.

Constraints:

    1 <= numCourses <= 1000
    0 <= prerequisites.length <= 1000
    prerequisites[i].length == 2
    0 <= a[i], b[i] < numCourses
    All prerequisite pairs are unique.



Topics


Recommended Time & Space Complexity

You should aim for a solution with O(V + E) time and O(V + E) space, where V is the number of courses (nodes) and E is the number of prerequisites (edges).

'''
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        in_degree = {}
        for c in range(numCourses):
            in_degree[c] = 0

        adj_list = defaultdict(list)

        for p in prerequisites:
            a, b = p
            in_degree[a] += 1
            adj_list[b].append(a)
        
        # print(f'{in_degree=}')
        # print(f'{adj_list=}')

        to_take = deque()
        for i in in_degree:
            if in_degree[i] == 0:
                to_take.append(i)

        taken = 0
        while to_take:
            course = to_take.popleft()
            taken += 1
            # print(f'taken {course=}')
            for dep in adj_list[course]:
                in_degree[dep] -= 1
                if in_degree[dep] == 0:
                    to_take.append(dep)
                
        return taken == numCourses


        