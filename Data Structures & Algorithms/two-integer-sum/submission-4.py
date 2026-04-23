class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hNums = {num: i for i, num in enumerate(nums)}
        for i,n in enumerate(nums):
            diff= target - n
            if diff in hNums and hNums[diff] != i:
                return [i, hNums[diff]]

        