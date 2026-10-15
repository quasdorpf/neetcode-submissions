class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for string in strs:
            freq = [0 for i in range(26)]
            for char in string:
                freq[ord(char)-97] +=1
            hash = tuple(freq)
            if anagrams.get(hash) is None:
                anagrams[hash] = [string]
            else:
                anagrams[hash].append(string)
        return list(anagrams.values())