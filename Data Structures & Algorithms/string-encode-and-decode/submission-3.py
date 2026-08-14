class Solution:
    # ord
    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        res = []
        
        for string in strs:
            tempString = [ord(char) for char in string]
            res.append(tempString)
        
        return str(res)

    # chr
    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        
        res = []
        lst = s[2:-2].split('], [')
        
        for wordList in lst:
            temp = wordList.split(',')
            resTemp = []
            #print(temp)

            for char in temp:
                if char:
                    resTemp.append(chr(int(char)))
                else:
                    resTemp.append("")
                #print(chr(int(char)))
            
            res.append(''.join(resTemp))
        
        return res
