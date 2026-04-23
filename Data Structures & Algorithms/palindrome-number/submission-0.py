class Solution:
    def isPalindrome(self, x: int) -> bool:
        xstr = str(x)
        xrev = xstr[::-1]
        return xstr == xrev 