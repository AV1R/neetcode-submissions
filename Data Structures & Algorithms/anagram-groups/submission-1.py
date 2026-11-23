class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 0:
            return [[""]]
        
        seen = {}
        for stri in strs:
            key = ''.join(sorted(stri))
            if key not in seen:
                seen[key] = [stri]
            else:
                seen[key].append(stri)
        return list(seen.values())