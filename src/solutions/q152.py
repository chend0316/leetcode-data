from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxSoFar = nums[0]
        maxToHere = minToHere = nums[0]
        for n in nums[1:]:
            tmp = [n, n * maxToHere, n * minToHere]
            maxToHere = max(tmp)
            minToHere = min(tmp)
            maxSoFar = max(maxSoFar, maxToHere)
        return maxSoFar
