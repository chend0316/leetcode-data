from typing import List
import math

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        res = math.inf
        for i in range(len(nums) - 2):
            j, k = i + 1, len(nums) - 1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                # print(i, j, k)
                res = s if abs(s - target) < abs(res - target) else res
                if s >= target: k -= 1
                else: j += 1
        return res
