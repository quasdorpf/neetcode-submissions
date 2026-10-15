class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for string in strs:
            chars = ''.join(sorted(string))
            if anagrams.get(chars) is None:
                anagrams[chars] = [string]
            else:
                anagrams[chars].append(string)
        return list(anagrams.values())