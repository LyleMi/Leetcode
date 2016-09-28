class Solution(object):
    def spiralOrder(self, matrix):
        ret = []
        while True:
            try:
                ret += matrix.pop(0)
                ret += [row.pop() for row in matrix]
                ret += matrix.pop()[::-1]
                ret += [row.pop(0) for row in matrix[::-1]]
            except:
                return ret
