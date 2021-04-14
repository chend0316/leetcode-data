from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if not nums: return 1
        i = 0
        while i < len(nums):
            j = nums[i] - 1
            if 0 <= j < len(nums) and nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1
        for i in range(len(nums)):
            if i + 1 != nums[i]:
                return i + 1
        return nums[-1] + 1