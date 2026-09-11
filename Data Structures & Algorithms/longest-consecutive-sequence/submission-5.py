class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        res = 0

        for num in nums:
            if num - 1 in nums:
                continue

            next_num = num + 1
            cur_res = 1
            while next_num in nums:
                cur_res += 1
                next_num += 1

            res = max(cur_res, res)
                
        return res 