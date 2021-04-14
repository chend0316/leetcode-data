from collections import defaultdict

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        res = 0
        resByIdx = defaultdict(int)
        stack = []

        for idx, c in enumerate(s):
            if c == '(':
                stack.append((c, idx))
            else:
                if stack and stack[-1][0] == c:
                    resByIdx[idx] = idx - stack[-1][1] + 1 + resByIdx[stack[-1][1]-1]
                    res = max(res, resByIdx[idx])
                    stack.pop()

        return res
