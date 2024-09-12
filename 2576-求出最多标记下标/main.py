class Solution:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        nums = sorted(nums)
        result = 0
        little = 0
        len_nums = len(nums)
        mid_start = len_nums // 2  # 6:3 5:2
        big = mid_start
        while little < mid_start and big < len_nums:
            while big < len_nums and nums[big] < nums[little] * 2:
                big += 1
            if big < len_nums:
                result += 2
            big += 1
            little += 1
        return result
