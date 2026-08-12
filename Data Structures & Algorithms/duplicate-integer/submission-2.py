class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        prevNum = None
        
        nums.sort()

        for num in nums:
            if prevNum == num:
                return True

            prevNum = num

        return False