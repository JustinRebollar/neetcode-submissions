class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicateChecker = set()

        for num in nums: 
            if num in duplicateChecker:
                return True

            duplicateChecker.add(num)

        return False