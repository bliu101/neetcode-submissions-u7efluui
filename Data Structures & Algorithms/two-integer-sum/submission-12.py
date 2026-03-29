class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numSet = set(nums)
        numsDict = {}
        for i, n in enumerate(nums):
            numsDict[n] = i

        for i, n in enumerate(nums):
            if (target - n) in numsDict and numsDict[target-n] != i:
                return [i, numsDict[target-n]]
