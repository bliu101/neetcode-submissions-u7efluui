class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # dict where key is the number and value is freq
        freqDict = {}
        for n in nums:
            freqDict[n] = freqDict.get(n, 0) + 1
        
        
        freqArray = []
        for key, value in freqDict.items():
            freqArray.append((value, key))
        freqArray.sort()
        result = []
        while k > 0:
            result.append(freqArray.pop()[1])
            k -= 1
        return result
