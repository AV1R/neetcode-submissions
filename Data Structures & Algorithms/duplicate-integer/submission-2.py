class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numsClean = list(set(nums))
        return len(numsClean) != len(nums)
        