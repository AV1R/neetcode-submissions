class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}                    # valor -> índice
        for i, num in enumerate(nums):
            diff = target - num
            if diff in seen: 
                # el complemento está en el pasado, nunca es el mismo elemento
                return [seen[diff], i]
            seen[num] = i