class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        numTracker = {}

        for num in nums:
            numTracker[num] = numTracker.get(num, 0) + 1

        return max(numTracker, key=numTracker.get)