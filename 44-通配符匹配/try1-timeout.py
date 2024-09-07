class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def check_match(target, pattern):
            if len(pattern) == 0:
                if len(target) > 0:
                    return False
                else:
                    return True
            else:
                if pattern[0] == '*':
                    return (
                            check_match(target, pattern[1:])
                            or (check_match(target[1:], pattern) if len(target) > 0 else False)
                    )
                elif pattern[0] == '?':
                    if len(target) > 0:
                        return check_match(target[1:], pattern[1:])
                    else:
                        return False
                else:
                    if len(target) > 0 and target[0] == pattern[0]:
                        return check_match(target[1:], pattern[1:])
                    else:
                        return False

        return check_match(s, p)
