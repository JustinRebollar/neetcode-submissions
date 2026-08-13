class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictionary = {}

        for num in nums:
            dictionary[num] = dictionary.get(num, 0) + 1

        return [sorted(dictionary.items(), key=lambda item: item[1], reverse=True)[val][0] for val in range(k)]