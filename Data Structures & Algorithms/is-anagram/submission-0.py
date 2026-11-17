class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            a = "".join(sorted(s))
            q = "".join(sorted(t))

            for i in range(0, len(s)):
                if a[i] != q[i]:
                    return False
            return True

        return False