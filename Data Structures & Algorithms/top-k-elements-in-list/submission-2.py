class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictionary = {}
        res = []

        for num in nums:
            dictionary[num] = dictionary.get(num, 0) + 1
        
        res = sorted([[value, key] for key, value in dictionary.items()])[-k:]

        for val in range(len(res)):
            res[val] = res[val][1]

        return res