class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {")": "(", "]": "[", "}": "{"}
        stack = []

        for ch in s:
            if ch in pairs:                       # is close 
                if not stack or stack.pop() != pairs[ch]:
                    return False                 
            else:
                stack.append(ch)                  # is open

        return len(stack) == 0
