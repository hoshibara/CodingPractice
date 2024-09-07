class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = []
        i = 0
        len_p = len(p)
        len_s = len(s)
        processed_p = []
        while i < len_p:
            if p[i] == '*':
                processed_p[-1] = processed_p[-1] + '*'
            else:
                processed_p.append(p[i])
            i += 1
        p = processed_p
        len_p = len(p)

        for i in range(len_p + 1):
            dp.append([False] * (len_s + 1))

        dp[0][0] = True

        for i in range(len_p):
            for j in range(len_s):
                if p[i] == '.':
                    if i + 1 <= len_p and j + 1 <= len_s:
                        dp[i + 1][j + 1] = dp[i + 1][j + 1] or dp[i][j]
                elif p[i][-1] == '*':
                    copy_char = p[i][0]
                    if copy_char == '.':
                        if i + 1 <= len_p and j + 1 <= len_s:
                            # 消耗掉*
                            dp[i + 1][j + 1] = dp[i + 1][j + 1] or dp[i][j]
                        if i + 1 <= len_p:
                            # 匹配0个字符
                            dp[i + 1][j] = dp[i + 1][j] or dp[i][j]
                        if j + 1 <= len_s:
                            # 下一个接着匹配*
                            dp[i][j + 1] = dp[i][j + 1] or dp[i][j]
                    else:
                        if copy_char == s[j] and i + 1 <= len_p and j + 1 <= len_s:
                            # 消耗掉*
                            dp[i + 1][j + 1] = dp[i + 1][j + 1] or dp[i][j]
                        if i + 1 <= len_p:
                            # 匹配0个字符
                            dp[i + 1][j] = dp[i + 1][j] or dp[i][j]
                        if copy_char == s[j] and j + 1 <= len_s:
                            # 下一个接着匹配*
                            dp[i][j + 1] = dp[i][j + 1] or dp[i][j]
                else:
                    if p[i] == s[j] and i + 1 <= len_p and j + 1 <= len_s:
                        dp[i + 1][j + 1] = dp[i + 1][j + 1] or dp[i][j]

        for i in range(len_p):
            if p[i][-1] == '*':
                dp[i + 1][-1] = dp[i + 1][-1] or dp[i][-1]

        return dp[-1][-1]
