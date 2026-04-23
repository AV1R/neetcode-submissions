class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        arrSort= sorted(list(set(nums)))
        lim=len(arrSort)-1
        if len(nums) == 0:
            return 0

        longCons=1
        currentLen=1
        i=0
        while i < lim:
            if arrSort[i+1] - arrSort[i] == 1:
                currentLen += 1
            else:
                currentLen = 1
            longCons = max(longCons, currentLen)
            i+=1

        return longCons