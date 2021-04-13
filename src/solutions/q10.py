class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n, m = len(s), len(p)
        dp = [[False]*(m+1) for _ in range(n+1)]
        dp[0][0] = True
        for j in range(m):
            if p[j] == '*':
                dp[0][j+1] = dp[0][j-1]

        for i in range(n):
            for j in range(m):
                if p[j] == '.' or p[j] == s[i]:
                    dp[i+1][j+1] = dp[i][j]
                elif p[j] == '*':
                    if j > 0 and (p[j-1] == '.' or p[j-1] == s[i]):
                        dp[i+1][j+1] = dp[i][j+1] or dp[i+1][j-1] or dp[i][j-1]
                    else:
                        dp[i+1][j+1] = dp[i+1][j-1]
                # else:
                #     dp[i+1][j+1] = False

        return dp[n][m]
