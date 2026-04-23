class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        positions=[]
        hashNums={}
    
        for i in range(len(nums)):
            hashNums[nums[i]]=i
        
        for i in range(len(nums)):
            diff=target - nums[i]
            if(diff in hashNums and hashNums[diff] != i):
                return [i, hashNums[diff]]        