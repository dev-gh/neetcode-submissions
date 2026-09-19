class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        weights = []
        for s in stones:
            heapq.heappush(weights, -s)
            
        while len(weights) > 1:
            x = heapq.heappop(weights)
            y = heapq.heappop(weights)

            if x == y:
                continue
            
            if x < y:
                heapq.heappush(weights, x - y)

        return 0 if len(weights) == 0 else -weights[0]
        