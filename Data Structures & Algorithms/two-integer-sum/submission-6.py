class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        storeNums={}
        for i,n in enumerate(nums):
            storeNums[n] = i

        for i,n in enumerate(nums):
            diff = target - n
            if diff in storeNums and storeNums[diff] != i:
                return [i, storeNums[diff]]
        
        return []