from typing import List
from heapq import nlargest
import operator

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_to_cnt = {}
        for num in nums:
            num_to_cnt.setdefault(num, 0)
            num_to_cnt[num] += 1
        num_cnt_tuples = [(cnt, num) for num, cnt in num_to_cnt.items()]
        return [num for cnt, num in nlargest(k, num_cnt_tuples, key=operator.itemgetter(0))]
