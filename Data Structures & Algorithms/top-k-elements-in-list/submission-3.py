import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_counter = Counter(nums)
        heap = []

        for num, count in num_counter.items():
            tup = tuple([count, num])

            if len(heap) < k:
                heapq.heappush(heap, tup)
            else: 
                heapq.heappushpop(heap, tup)

        return [num for count, num in heap]
