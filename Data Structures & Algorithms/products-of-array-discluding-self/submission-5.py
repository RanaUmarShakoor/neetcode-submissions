class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        pr = 1
        fz = 0
        ml = False
        for n in nums:
            if n == 0:
                fz = fz + 1
            else:
                pr = pr * n
                ml = True

        if not ml:
            pr = 0

        for i in range(len(nums)):
            if fz:
                if nums[i] == 0 and fz == 1:
                    res.append(pr)
                elif nums[i] == 0 and fz > 1:
                    res.append(0)
                else:
                    res.append(0)
            else:
                res.append(pr//nums[i])

        return res
