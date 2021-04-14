from collections import defaultdict
from typing import List

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        target = defaultdict(int)
        n, k = len(words), len(words[0])
        for word in words:
            target[word] += 1
        res = []        

        for i in range(0, len(s) - n * k + 1):
            length = 0
            cnt = defaultdict(int)
            for j in range(n):
                sect = s[i+j*k:i+(j+1)*k]
                cnt[sect] += 1
                if sect not in target or target[sect] < cnt[sect]:
                    break
                length += 1
            if length == n: res.append(i)
        
        return res
