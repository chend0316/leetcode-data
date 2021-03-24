from typing import List
import math

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # dp[2][0] 表示卖了2次，目前手上无股票
        # dp[1][1] 表示卖了1次，目前手上有股票
        dp = [[0 for _ in range(2)] for _ in range(3)]
        dp[0][1] = dp[1][1] = dp[2][1] = -math.inf

        for price in prices:
            tmp = [[0 for _ in range(2)] for _ in range(3)]
            for i in range(3):
                if i == 0:
                    tmp[i][0] = dp[i][0]
                else:
                    tmp[i][0] = max(dp[i][0], dp[i-1][1] + price)
                tmp[i][1] = max(dp[i][1], dp[i][0] - price)
            dp = tmp
            # print(dp)

        res = 0
        for row in dp:
            res = max(res, max(row))
        return res
