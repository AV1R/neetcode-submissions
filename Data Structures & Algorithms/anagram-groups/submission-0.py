class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashStrs=defaultdict(list)
        for s in strs:
            sortedS = ''.join(sorted(s))
            hashStrs[sortedS].append(s)
        return list(hashStrs.values())
