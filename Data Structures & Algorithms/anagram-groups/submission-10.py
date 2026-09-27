from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for string in strs:
            str_index = [0] * 26

            for char in string:
                char_index = ord(char) - ord('a')
                str_index[char_index] += 1

            res[tuple(str_index)].append(string)

        return[value for key, value in res.items()]