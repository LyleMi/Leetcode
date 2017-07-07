class Solution(object):

    def lengthOfLongestSubstring(self, s):
        res = 0, start = 0
        dic = {}
        for i, ch in enumerate(s):
            if ch in dic:
                res = max(res, i - start)
                start = max(start, dic[ch] + 1)
            dic[ch] = i
        return max(res, len(s) - start)
