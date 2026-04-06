class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # find the beginning of the sequences:
        #   if the num-1 does not exist in the array, then its the beginning
        # loop thru the sequence comparing size
        numSet = set(nums)
        if not nums:
            return 0
        maxLen = 1
        for n in nums:
            if n-1 not in numSet:
                currLen = 1
                while n + 1 in numSet:
                    currLen += 1
                    maxLen = max(currLen, maxLen)
                    n += 1
        return maxLen
        
                