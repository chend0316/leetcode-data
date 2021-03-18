# 测试用例存在多解的情况

class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ''
        for i in range(len(s)):
            l = r = i
            while l >= 0 and r < len(s):
                if s[l] != s[r]: break
                if r - l + 1 > len(res): res = s[l: r+1]
                l, r = l - 1, r + 1
            l, r = i, i + 1
            while l >= 0 and r < len(s):
                if s[l] != s[r]: break
                if r - l + 1 > len(res): res = s[l: r+1]
                l, r = l - 1, r + 1
        return res
