class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            # a = "".join(sorted(s))
            # q = "".join(sorted(t))

            # for i in range(0, len(s)):
            #     if a[i] != q[i]:
            #         return False
            # return True

            z = {}
            x = {}
            for i in range(len(s)):
                z[s[i]] = 1 + z.get(s[i], 0)
                x[t[i]] = 1 + x.get(t[i], 0)
            
            return z == x

        return False