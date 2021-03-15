from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.ans = []
        self.n = n
        self.dfs(k, 1, [])
        return self.ans
    
    def dfs(self, k, start, path):
        if k == 0:
            self.ans.append(path[:])
            return
        if start > self.n: return

        for i in range(start, self.n + 1):
            self.dfs(k - 1, i + 1, path + [i])
