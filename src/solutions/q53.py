from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSoFar = nums[0]
        maxToHere = nums[0]
        for n in nums[1:]:
            maxToHere = maxToHere + n if maxToHere > 0 else n
            maxSoFar = max(maxSoFar, maxToHere)
        return maxSoFar
