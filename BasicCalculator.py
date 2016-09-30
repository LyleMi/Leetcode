class Solution(object):

    def calculate(self, s):

        i = 0
        result = 0
        signs = [1, 1]

        while i < len(s):
            c = s[i]
            if c.isdigit():
                start = i
                while i < len(s) and s[i].isdigit():
                    i += 1
                result += signs.pop() * int(s[start:i])
                i -= 1
            elif c in "+(-":
                signs += signs[-1] * (1, -1)[c == '-'],
            elif c in ")":
                signs.pop()
            i += 1

        return result
