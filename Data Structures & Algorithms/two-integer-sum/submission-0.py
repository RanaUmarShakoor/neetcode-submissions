class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        for i in range(len(nums)):
            k = target - nums[i]
            if k in h:
                return [h[k], i]
            else:
                h[nums[i]] = i 
        return []