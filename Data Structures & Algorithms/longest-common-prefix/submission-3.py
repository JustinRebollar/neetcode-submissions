class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        commonPrefix = list(strs[0])

        for i in range(1, len(strs)):
            currStr = list(strs[i])

            for iTwo in range(len(commonPrefix)):
                if len(commonPrefix) == 0 or len(currStr) == 0:
                    return ''

                if iTwo < len(commonPrefix) and iTwo < len(currStr):
                    if commonPrefix[iTwo] != currStr[iTwo]:
                        del commonPrefix[iTwo:]
                        continue
                else:
                    del commonPrefix[(iTwo):]


        return ''.join(commonPrefix)