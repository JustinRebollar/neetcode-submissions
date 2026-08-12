class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        resMap = {}

        for string in strs:
            sortedString = sorted(string)

            key = ''.join(sortedString)
            current_list = resMap.get(key, [])
            current_list.append(string)
            resMap[key] = current_list

        return [group for group in resMap.values()]
