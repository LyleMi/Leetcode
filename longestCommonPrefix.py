class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs: return ""
        pre = strs[0]
        for i in range(len(pre)):
            for s in strs:
                if i >= len(s) or pre[i] != s[i]:
                    return pre[0:i]
        return pre