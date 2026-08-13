class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        sorted = False
        editedThisRun = False

        i = 0

        while not sorted:
            if len(nums) == 1:
                break

            if i == (len(nums) - 1):
                if not editedThisRun:
                    break

                i = 0
                editedThisRun = False

            if nums[i] > nums[i + 1]:
                temp = nums[i]
                nums[i] = nums[i + 1]
                nums[i + 1] = temp
                editedThisRun = True
            
            i += 1

        return nums
