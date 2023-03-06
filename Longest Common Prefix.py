class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        sol = ""
        least = min(len(string) for string in strs)
        if least > 0:
            pre = strs[0][0]
        else:
            return ""

        for it in range(0, least ):
            for item in strs:
                if item[it] != pre[it]:
                    return sol
            sol = pre
            if it + 1 < least:
                pre += strs[0][it + 1] 
            else:
                return sol   
