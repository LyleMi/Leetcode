class Solution(object):

    def generateParenthesis(self, n):
        l = list()
        def backtrack(l, s, start, end, n):
            if len(s) == (n << 1):
                l.append(s)
                return
            if start < n:
                backtrack(l, s + "(", start + 1, end, n)
            if end < start:
                backtrack(l, s + ")", start, end + 1, n)
        backtrack(l, "", 0, 0, n)
        return l
