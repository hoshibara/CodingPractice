class Solution:
    def clearDigits(self, s: str) -> str:
        if_delete = True
        while if_delete:
            if_delete = False
            for i in range(len(s)):
                if '0' <= s[i] <= '9':
                    s = s[:i - 1] + s[i + 1:]
                    if_delete = True
                    break
        return s
