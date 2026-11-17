class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        h = {}
        for n in nums:
            h[n] = 1 + h.get(n, 0)

        z = sorted(h.keys(), key=lambda x: h[x], reverse=True)

        return z[:k]
