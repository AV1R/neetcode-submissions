class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lenNums=len(nums)
        output=list()

        i=0
        while len(output) != lenNums:
            extractArr= nums[:]
            extractArr.pop(i)
            productIdx=1
            for num in extractArr:
                productIdx*= num
            output.append(productIdx)
            i+=1
        return output