class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h={}
        for string in strs:
            sorted_string=''.join(sorted(string))
            if sorted_string not in h:
                h[sorted_string]=[]
            h[sorted_string].append(string)
        return list(h.values())