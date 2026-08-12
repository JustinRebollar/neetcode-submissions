class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(s):
            return False

        key = {}

        for char in s:
            key[char] = key.get(char, 0) + 1
        
        for char in t:
            key[char] = key.get(char, 0) - 1


        return all(x == 0 for x in key.values())