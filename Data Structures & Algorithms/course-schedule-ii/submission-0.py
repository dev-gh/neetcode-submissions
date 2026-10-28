'''
ou are given an array prerequisites where prerequisites[i] = [a, b] indicates that you must take course b first if you want to take course a.

    For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.

There are a total of numCourses courses you are required to take, labeled from 0 to numCourses - 1.

Return a valid ordering of courses you can take to finish all courses. If there are many valid answers, return any of them. If it's not possible to finish all courses, return an empty array.

Example 1:

Input: numCourses = 3, prerequisites = [[1,0]]

Output: [0,1,2]

Explanation: We must ensure that course 0 is taken before course 1.

Example 2:

Input: numCourses = 3, prerequisites = [[0,1],[1,2],[2,0]]

Output: []

Explanation: It's impossible to finish all courses.

Constraints:

    1 <= numCourses <= 1000
    0 <= prerequisites.length <= 1000
    All prerequisite pairs are unique.

'''
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        in_degree = [0] * numCourses
        adjacents = defaultdict(list)

        for course, prereq in prerequisites:
            adjacents[prereq].append(course)
            in_degree[course] += 1

        no_prereqs = deque()
        for c in range(len(in_degree)):
            if in_degree[c] == 0:
                no_prereqs.append(c)

        print(f'{in_degree=}, {adjacents=}, {no_prereqs=}')
        result = []
        while no_prereqs:
            crs = no_prereqs.popleft()
            result.append(crs)

            for dep in adjacents[crs]:
                in_degree[dep] -= 1
                if in_degree[dep] == 0:
                    no_prereqs.append(dep)
                

        return [] if len(result) != numCourses else result

        