'''
You are given an array of CPU tasks tasks, where tasks[i] is an uppercase english character from A to Z. You are also given an integer n.

Each CPU cycle allows the completion of a single task, and tasks may be completed in any order.

The only constraint is that identical tasks must be separated by at least n CPU cycles, to cooldown the CPU.

Return the minimum number of CPU cycles required to complete all tasks.

Example 1:

Input: tasks = ["X","X","Y","Y"], n = 2

Output: 5

Explanation: A possible sequence is: X -> Y -> idle -> X -> Y.

Example 2:

Input: tasks = ["A","A","A","B","C"], n = 3

Output: 9

Explanation: A possible sequence is: A -> B -> C -> Idle -> A -> Idle -> Idle -> Idle -> A.

Constraints:

    1 <= tasks.length <= 10000
    0 <= n <= 100

'''
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freqs = [0] * 26
        for t in tasks:
            freqs[ord(t) - ord('A')] += 1

        scheduler = []
        index = 0
        for f in freqs:
            if f > 0:
                heapq.heappush(scheduler, (-f, index))

            index += 1

        cycles = 0
        while len(scheduler) > 0:
            rounds = n + 1 if len(scheduler) > n + 1 else len(scheduler)
            tasks_count = rounds
            incomplete_tasks = []
            while rounds > 0:
                neg_freq, name = heapq.heappop(scheduler)
                if neg_freq < -1:
                    incomplete_tasks.append((neg_freq + 1, name))
                rounds -= 1

            for i_task in incomplete_tasks:
                heapq.heappush(scheduler, i_task)

            if len(incomplete_tasks) > 0:
                    cycles += n + 1
            else:
                cycles += tasks_count
        
        return cycles







        