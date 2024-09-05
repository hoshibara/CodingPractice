class Solution:
    def trap(self, height: List[int]) -> int:
        left_max = [0] * len(height)
        right_max = [0] * len(height)
        tmp_max = 0
        for i in range(0, len(height)):
            tmp_max = max(tmp_max, height[i])
            left_max[i] = tmp_max
        tmp_max = 0
        for i in range(len(height) - 1, -1, -1):
            tmp_max = max(tmp_max, height[i])
            right_max[i] = tmp_max
        # print(left_max)
        # print(right_max)
        for i in range(0, len(height)):
            height[i] = min(left_max[i], right_max[i]) - height[i]
        print(height)
        return sum(height)
