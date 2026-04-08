class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # bst on array 1 to max(piles)
        minTime = 0
        l, r = 1, max(piles)

        while l <= r:
            m = l + (r - l) // 2
            totalTime = 0

            for bananas in piles:
                totalTime += math.ceil(bananas / m)
            
            if totalTime <= h:
                minTime = m
                r = m - 1
            else:
                l = m + 1

        return minTime



