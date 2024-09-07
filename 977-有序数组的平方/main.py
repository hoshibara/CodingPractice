class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        mid = 0
        len_nums = len(nums)
        while mid < len_nums and nums[mid] < 0:
            mid += 1
        right = mid
        left = mid - 1
        result = []
        while right < len_nums and left >= 0:
            if -nums[left] >= nums[right]:
                result.append(nums[right] * nums[right])
                right += 1
            else:
                result.append(nums[left] * nums[left])
                left -= 1
        while right < len_nums:
            result.append(nums[right] * nums[right])
            right += 1
        while left >= 0:
            result.append(nums[left] * nums[left])
            left -= 1
        return result
