from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        self.recursive(nums, [])
        return self.ans
    
    def recursive(self, nums, path):
        if not nums: self.ans.append(path)
        for idx in range(len(nums)):
            num = nums.pop(idx)
            self.recursive(nums, path + [num])
            nums.insert(idx, num)
