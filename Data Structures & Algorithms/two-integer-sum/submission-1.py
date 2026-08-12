class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for iTwo in range(len(nums)):
                if nums[i] + nums[iTwo] == target and i != iTwo:
                    return [i, iTwo]
