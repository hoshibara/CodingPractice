class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        dp = []
        for i in range(k + 1):
            dp.append([1] * len(nums))
        for i in range(k + 1):
            for u in range(len(nums)):
                for v in range(u + 1, len(nums)):
                    if nums[u] == nums[v]:
                        dp[i][v] = max(dp[i][u] + 1, dp[i][v])
                    elif i < k:
                        dp[i + 1][v] = max(dp[i][u] + 1, dp[i + 1][v])
        return max(map(lambda x: max(x), dp))
