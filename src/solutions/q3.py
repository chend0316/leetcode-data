import collections

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        l = r = 0
        res = 0
        counter = collections.defaultdict(int)
        while r < len(s):
            while counter[s[r]] >= 1:
                counter[s[l]] -= 1
                l += 1
            counter[s[r]] += 1
            res = max(res, r - l + 1)
            r += 1
        return res
