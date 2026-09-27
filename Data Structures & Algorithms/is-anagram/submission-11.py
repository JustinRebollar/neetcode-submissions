class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_len = len(s)
        t_len = len(t)
        
        s_counter = [0] * 26
        t_counter = [0] * 26

        for char in s:
            index =  ord(char) - ord('a')
            s_counter[index] += 1

        for char in t:
            index =  ord(char) - ord('a')
            t_counter[index] += 1

        return s_counter == t_counter