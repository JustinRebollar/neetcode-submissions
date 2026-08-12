class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicateChecker = []

        for num in nums: 
            if num in duplicateChecker:
                return True

            duplicateChecker.append(num)

        return False