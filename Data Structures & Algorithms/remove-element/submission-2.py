class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        originalCount = len(nums)
        numMatched = 0
        matchedIndeces = []

        for i in range(len(nums)):
            if nums[i] == val:
                matchedIndeces.append(i)
                numMatched += 1
                
        for i in reversed(matchedIndeces):
            nums.pop(i)
        
        return originalCount - numMatched