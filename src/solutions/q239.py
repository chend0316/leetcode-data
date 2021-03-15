import collections
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        que = collections.deque()
        n = len(nums)
        res = []
        for r in range(n):
            l = r - k + 1
            while que and nums[que[-1]] <= nums[r]: que.pop()
            que.append(r)
            if que[0] == l - 1: que.popleft()
            if l >= 0: res.append(nums[que[0]])
        return res
