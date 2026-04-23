class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ssetln= len(list(set(s)))
        tsetln= len(list(set(t)))
        if ssetln != tsetln:
            return False

        freqs = {}
        freqt = {}

        for char in s:
            if freqs.get(char):
                freqs[char] = freqs[char] + 1
            else:
                freqs[char] =  1

        for char in t:
            if freqt.get(char):
                freqt[char] = freqt[char] + 1
            else:
                freqt[char] =  1

        for k in freqt.keys():
            if not freqt.get(k) or not freqs.get(k):
                return False
            if freqt[k] != freqs[k]:
                return False

        return True