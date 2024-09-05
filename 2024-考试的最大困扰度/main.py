class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        len_answer = len(answerKey)
        # count T
        head = 0
        tail = 0
        count_f = 0
        max_len = 0
        while tail < len_answer:
            if answerKey[tail] == 'F':
                count_f += 1
            tail += 1
            if count_f > k:
                while answerKey[head] != 'F':
                    head += 1
                head += 1
                count_f -= 1
            max_len = max(max_len, tail - head)

        # count F
        head = 0
        tail = 0
        count_t = 0
        while tail < len_answer:
            if answerKey[tail] == 'T':
                count_t += 1
            tail += 1
            if count_t > k:
                while answerKey[head] != 'T':
                    head += 1
                head += 1
                count_t -= 1
            max_len = max(max_len, tail - head)

        return max_len
