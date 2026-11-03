'''
You are given a 2-D integer array points, where points[i] = [xi, yi]. Each points[i] represents a distinct point on a 2-D plane.

The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between the two points, i.e. |xi - xj| + |yi - yj|.

Return the minimum cost to connect all points together, such that there exists exactly one path between each pair of points.

Example 1:

Input: points = [[0,0],[2,2],[3,3],[2,4],[4,2]]

Output: 10

Constraints:

    1 <= points.length <= 1000
    -1,000,000 <= xi, yi <= 1,000,000
    All pairs (xi, yi) are distinct.

'''
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        # Prim's algo

        adjacency = defaultdict(list)

        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                ax, ay = points[i]
                bx, by = points[j]
                adjacency[i].append((abs(ax - bx) + abs(ay - by), j))
                adjacency[j].append((abs(ax - bx) + abs(ay - by), i))
            
        # print(f'{adjacency=}')

        idx = 0
        stack = adjacency[idx][:] # copy to not mutate
        heapq.heapify(stack)
        visited = set()
        visited.add(idx)

        distance = 0
        while stack:
            dist, neigh = heapq.heappop(stack)
            
            if neigh not in visited:
                distance += dist
                visited.add(neigh)
                for n in adjacency[neigh]:
                    heapq.heappush(stack, n)


        return distance
                





        