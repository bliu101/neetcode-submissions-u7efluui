class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i, n in enumerate(nums):
            if n > 0: # negative value so can't make 0
                break
            if i > 0 and n == nums[i - 1]: # no duplicates
                continue
            
            l, r = i + 1, len(nums)-1
            while l < r:
                threeSum = nums[l] + nums[r] + n
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([nums[l], nums[r], n])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res
                