class Solution:
    def sumDigitDifferences(self, nums: List[int]) -> int:
        num_bit_count = len(str(nums[0]))
        per_bit_count = []
        for i in range(num_bit_count):
            per_bit_count.append([0] * 10)
        for i in range(len(nums)):
            str_num = str(nums[i])
            for j in range(len(str_num)):
                per_bit_count[j][int(str_num[j])] += 1
        # print(per_bit_count)

        result = 0
        for i in range(num_bit_count):
            bit_result = 0
            all_num_sum = sum(per_bit_count[i])
            for j in range(10):
                bit_result += per_bit_count[i][j] * (all_num_sum - per_bit_count[i][j])
            result += bit_result // 2

        return result
