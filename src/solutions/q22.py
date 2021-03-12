from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrace(l, r, path):
            if l == r == 0: res.append(path)
            else:
                if l > 0: backtrace(l - 1, r, path + '(')
                if r > l: backtrace(l, r - 1, path + ')')
        backtrace(n, n, '')
        return res
