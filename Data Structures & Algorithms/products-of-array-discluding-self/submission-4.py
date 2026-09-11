class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        list_length = len(nums)
        res = [1] * list_length

        for i in range(1, list_length):
            res[i] = res[i - 1] * nums[i - 1]

        suffix = 1
        for i in range(list_length - 1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]
        
        return res