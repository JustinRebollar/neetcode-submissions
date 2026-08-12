class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        key = {}

        for i in range(len(s)):
            key[s[i]] = key.get(s[i], 0) + 1
            key[t[i]] = key.get(t[i], 0) - 1

        return all(value == 0 for value in key.values())