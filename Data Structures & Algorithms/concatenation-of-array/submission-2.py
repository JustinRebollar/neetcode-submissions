class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        res = []
        concatNum = 2

        for i in range(concatNum):
            for i in range(len(nums)):
                res.append(nums[i])
        
        return res