from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.ans = []
        nums = sorted(nums)
        self.nSum(nums, 4, target, [])
        return self.ans
        
    def nSum(self, nums, N, target, prefix):
        if N == 2:
            i, j = 0, len(nums) - 1
            while i < j:
                s = nums[i] + nums[j]
                if s == target:
                    self.ans.append(prefix + [nums[i], nums[j]])
                if s <= target:
                    i += 1
                    while i < j and nums[i] == nums[i-1]: i += 1
                if s >= target:
                    j -= 1
                    while i < j and nums[j] == nums[j+1]: j -= 1
        else:
            for i in range(len(nums) - (N - 1)):
                if i > 0 and nums[i] == nums[i-1]: continue
                self.nSum(nums[i+1:], N - 1, target - nums[i], prefix + [nums[i]])