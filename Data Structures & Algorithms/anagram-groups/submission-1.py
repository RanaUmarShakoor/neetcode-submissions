class Solution:
    def checkAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            z = {}
            x = {}
            for i in range(len(s)):
                z[s[i]] = 1 + z.get(s[i], 0)
                x[t[i]] = 1 + x.get(t[i], 0)
                
            return z == x

        return False

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h = {}

        for s in strs:
            k = ''.join(sorted(s))
            if k in h:
                h[k].append(s)
            else:
                h[k] = [s]
        
        return list(h.values())

    