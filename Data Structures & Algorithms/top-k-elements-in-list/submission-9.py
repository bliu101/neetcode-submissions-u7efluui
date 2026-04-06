class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqDict = {}
        for n in nums:
            freqDict[n] = 1 + freqDict.get(n, 0)

        heap = []
        for num in freqDict.keys(): # populate heap with freqDict key value
            heapq.heappush(heap, (freqDict[num], num))
            if len(heap) > k: # keep popping off the minimum so your left with the top k most freq
                heapq.heappop(heap)
        
        res = []
        while k > 0:
            res.append(heapq.heappop(heap)[1])
            k -= 1
        return res