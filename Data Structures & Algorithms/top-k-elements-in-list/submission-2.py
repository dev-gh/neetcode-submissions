from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        occurences = defaultdict(int)

        for n in nums:
            occurences[n] += 1

        # buckets for occurences starting from 0
        buckets = [[] for _ in range(len(nums) + 1)]

        for num, occurence in occurences.items():
            buckets[occurence].append(num)

        result = list()
        for b in range(len(buckets) - 1, 0, -1):
            #print(f'{len(buckets)=}, {b=}')
            if len(buckets[b]) != 0:
                # what if there are more than k elements in most frequent list?
                result += buckets[b]
                print(f'{result=}')
                if len(result) >= k:
                    break
                    
        return result


            

        