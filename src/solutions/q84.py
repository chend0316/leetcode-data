from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights = heights + [0]
        height_stack = [0]
        idx_stack = [-1]
        res = 0
        for i, h in enumerate(heights):
            while height_stack and height_stack[-1] > h:
                idx_stack.pop()
                res = max(res, height_stack.pop() * (i - idx_stack[-1] - 1)) 
            height_stack.append(h)
            idx_stack.append(i)
        return res
