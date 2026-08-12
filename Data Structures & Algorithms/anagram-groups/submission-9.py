class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        resMap = {}

        for string in strs:
            count = [0] * 26

            for char in string:
                count[ord(char) - ord('a')] += 1

            key = tuple(count)

            if key not in resMap:
                resMap[key] = []

            resMap[key].append(string)

        return list(resMap.values())
