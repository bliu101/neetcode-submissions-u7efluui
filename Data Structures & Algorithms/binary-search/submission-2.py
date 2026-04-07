class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1

        while l <= r:
            m = l + ((r-l) // 2) # find the middle

            if nums[m] > target: # if middle is greater than target, decr right
                r = m - 1
            elif nums[m] < target: # if middle is less than target, incr left
                l = m + 1
            else: # middle = target, return
                return m
        return -1