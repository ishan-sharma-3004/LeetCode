class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map={}
        for i in strs:
            sorted_word=''.join(sorted(i))
            map[sorted_word].append(i)
        return list(map.values())