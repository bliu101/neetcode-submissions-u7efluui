class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        alphaDictS, alphaDictT = {}, {}

        for i in range(len(s)):
            alphaDictS[s[i]] = 1 + alphaDictS.get(s[i], 0)
            alphaDictT[t[i]] = 1 + alphaDictT.get(t[i], 0)
        return alphaDictS == alphaDictT
