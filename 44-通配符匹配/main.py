class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = []
        len_p = len(p)
        len_s = len(s)
        if len_p == 0 and len_s == 0:
            return True
        if len_p == 0:
            return False
        if len_s == 0:
            if all(map(lambda x: x == "*", p)):
                return True
            else:
                return False

        for i in range(len_p + 1):
            dp.append([0] * (len_s + 1))
        for i in range(len_p):
            for j in range(len_s):
                if p[i] == "?":
                    dp[i][j] = 1
                elif p[i] == "*":
                    dp[i][j] = 2
                elif p[i] == s[j]:
                    dp[i][j] = 1
        for i in range(len_p):
            if p[i] == '*':
                dp[i][-1] = 2

        search = [(0, 0)]
        head = 0
        tail = 1

        while head < tail:
            u, v = search[head]
            if dp[u][v] == 1:
                if u + 1 < len_p + 1 and v + 1 < len_s + 1:
                    search.append((u + 1, v + 1))
                    tail += 1
            elif dp[u][v] == 2:
                if u + 1 < len_p + 1:
                    search.append((u + 1, v))
                    tail += 1
                if v + 1 < len_s + 1:
                    search.append((u, v + 1))
                    tail += 1
                if u + 1 < len_p + 1 and v + 1 < len_s + 1:
                    search.append((u + 1, v + 1))
                    tail += 1
            dp[u][v] = -1
            head += 1

        if dp[-1][-1] == -1:
            return True
        else:
            return False
