class Solution:
    def countWays(self, nums: List[int]) -> int:
        nums = sorted(nums)
        result = 0
        if 0 < nums[0]:
            result += 1
        for i in range(1, len(nums)):
            if nums[i - 1] < i < nums[i]:
                result += 1
        if len(nums) > nums[-1]:
            result += 1
        return result
