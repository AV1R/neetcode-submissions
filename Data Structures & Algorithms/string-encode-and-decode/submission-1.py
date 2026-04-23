class Solution:

    def encode(self, strs: List[str]) -> str:
        encodestr=""
        for char in strs:
            encodestr+=char+"."
        return encodestr

    def decode(self, s: str) -> List[str]:
        decodeStrList=list()
        decstr=""
        for char in s:
            if char != ".":
                decstr+=char
            else:
                decodeStrList.append(decstr)
                decstr=""
        return decodeStrList