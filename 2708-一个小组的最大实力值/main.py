class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        max_result = [0] * (len(nums))
        min_result = [0] * (len(nums))
        max_result[0] = nums[0]
        min_result[0] = nums[0]
        for i in range(1, len(nums)):
            max_result[i] = max(
                max_result[i - 1],
                max_result[i - 1] * nums[i],
                min_result[i - 1] * nums[i],
                nums[i],
            )
            min_result[i] = min(
                min_result[i - 1],
                max_result[i - 1] * nums[i],
                min_result[i - 1] * nums[i],
                nums[i],
            )
        return max(max_result[-1], min_result[-1])
