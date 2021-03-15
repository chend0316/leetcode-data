class Solution:
    def nthUglyNumber(self, n: int) -> int:
        if n <= 0: return 0
        ugly_nums = [1]
        prime_nums = [2, 3, 5]
        idx = [0, 0, 0]
        K = 3
        for _ in range(n - 1):
            candidate_nums = [prime_nums[i] * ugly_nums[idx[i]] for i in range(K)]
            candidate_min = min(candidate_nums)
            ugly_nums.append(candidate_min)
            for i in range(K):
                if candidate_nums[i] == candidate_min:
                    idx[i] += 1
        return ugly_nums[-1]
