class Solution:
    def isValid(self, s: str) -> bool:
        map = { ')': '(', ']': '[', '}': '{' }
        stack = ['#']
        for c in s:
            if c not in map: stack.append(c)
            elif stack.pop() != map[c]: return False
        return len(stack) == 1
